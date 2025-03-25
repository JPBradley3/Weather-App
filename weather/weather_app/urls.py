from django.urls import path
from . import views

urlpatterns = [
    path('', views.weather_map, name='weather_map'),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('set-location/', views.set_location, name='set_location'),
]
