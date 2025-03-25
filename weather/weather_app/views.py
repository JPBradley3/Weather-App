from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from .forms import SignUpForm, LocationForm
from .models import UserProfile
import requests
import os
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            next_url = request.POST.get('next', '')
            if next_url:
                return redirect(next_url)
            return redirect('weather_map')
        else:
            return render(request, 'weather_app/login.html', {
                'error_message': 'Invalid username or password.'
            })
    
    return render(request, 'weather_app/login.html', {
        'next': request.GET.get('next', '')
    })

def logout_view(request):
    logout(request)
    return redirect('weather_map')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            UserProfile.objects.create(user=user)
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('set_location')
    else:
        form = SignUpForm()
    return render(request, 'weather_app/signup.html', {'form': form})

@login_required
def set_location(request):
    try:
        profile = request.user.userprofile
    except UserProfile.DoesNotExist:
        profile = UserProfile.objects.create(user=request.user)

    if request.method == 'POST':
        form = LocationForm(request.POST, instance=profile)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.latitude = request.POST.get('latitude')
            profile.longitude = request.POST.get('longitude')
            profile.save()
            messages.success(request, 'Location updated successfully!')
            return redirect('weather_map')
    else:
        form = LocationForm(instance=profile)

    return render(request, 'weather_app/set_location.html', {'form': form})

@login_required
def weather_map(request):
    try:
        api_key = os.getenv('OPENWEATHER_API_KEY')
        if not api_key:
            raise ValueError("OpenWeather API key not found")
            
        profile = request.user.userprofile
        
        # Use user's location if set, otherwise default to Seattle
        lat = str(profile.latitude) if profile.latitude else "47.6062"
        lon = str(profile.longitude) if profile.longitude else "-122.3321"
        location_name = profile.location_name if profile.location_name else "Seattle"
        
        # Get current weather data
        weather_url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        response = requests.get(weather_url)
        response.raise_for_status()  # Raise an exception for bad status codes
        weather_data = response.json()

        # Get 5 day / 3 hour forecast data (free tier API)
        forecast_url = f"https://api.openweathermap.org/data/2.5/forecast?lat={lat}&lon={lon}&appid={api_key}&units=metric"
        forecast_response = requests.get(forecast_url)
        forecast_response.raise_for_status()
        forecast_data = forecast_response.json()

        # Process forecast data for the timeline
        timeline_data = []
        if 'list' in forecast_data:
            for item in forecast_data['list'][:8]:  # Next 24 hours (8 x 3-hour intervals)
                time = datetime.fromtimestamp(item['dt']).strftime('%H:%M')
                # Calculate precipitation probability (pop)
                pop = item.get('pop', 0) * 100  # Convert probability to percentage
                timeline_data.append({
                    'time': time,
                    'probability': pop,
                    'temp': item['main']['temp'],
                    'description': item['weather'][0]['description'],
                    'icon': item['weather'][0]['icon']
                })

        context = {
            'weather_data': weather_data,
            'timeline_data': timeline_data,
            'api_key': api_key,
            'location_name': location_name,
            'latitude': lat,
            'longitude': lon,
        }
        return render(request, 'weather_app/weather_map.html', context)
    except requests.RequestException as e:
        return render(request, 'weather_app/weather_map.html', {
            'error': f"Weather service error: {str(e)}"
        })
    except Exception as e:
        return render(request, 'weather_app/weather_map.html', {
            'error': f"An error occurred: {str(e)}"
        })

def index(request):
    if request.user.is_authenticated:
        return redirect('weather_map')
    return render(request, 'weather_app/index.html')
