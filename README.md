# Weather App

## Description
The Weather App is a web application that provides real-time weather information for various locations. Designed as part of the CS50W Capstone Project, this app aims to offer a clean and user-friendly interface to display accurate and up-to-date weather data.

## Features
- **Search Weather by Location**: Enter the name of a city or region to retrieve detailed weather information.
- **Current Weather Details**: View temperature, humidity, wind speed, and other weather metrics.
- **Forecast**: Access weather forecasts for the upcoming days.
- **Responsive Design**: Optimized for both desktop and mobile devices.

## Installation
1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/CS50w-Capstone.git
    ```
2. Navigate to the project folder:
    ```bash
    cd weather
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```
4. Set up API keys:
    - Obtain an API key from [OpenWeather](https://openweathermap.org/).
    - Add the API key to the environment variables or the application's configuration file.

## Running Locally
Follow the steps below based on your operating system:

### macOS
1. Open the Terminal.
2. Navigate to the project folder:
    ```bash
    cd ~/Documents/CS50w-Capstone/weather
    ```
3. Run the development server:
    ```bash
    python manage.py runserver
    ```
4. Access the app through `http://127.0.0.1:8000` in your browser.

### Windows (PowerShell)
1. Open PowerShell.
2. Navigate to the project folder:
    ```bash
    cd C:\Users\YourName\Documents\CS50w-Capstone\weather
    ```
3. Run the development server:
    ```bash
    python manage.py runserver
    ```
4. Access the app through `http://127.0.0.1:8000` in your browser.

### Linux
1. Open the terminal.
2. Navigate to the project folder:
    ```bash
    cd ~/CS50w-Capstone/weather
    ```
3. Run the development server:
    ```bash
    python manage.py runserver
    ```
4. Access the app through `http://127.0.0.1:8000` in your browser.

## Usage
- Visit the local development server URL (e.g., `http://127.0.0.1:8000`).
- Use the search bar to enter a location and view weather details.

## Technologies Used
- **Backend**: Django
- **Frontend**: HTML, CSS, JavaScript
- **Frameworks**: Django, Bootstrap (or any other frontend framework you use)
- **APIs**: OpenWeather
- **Database**: SQLite (or other)

## Future Enhancements
- Add support for additional weather APIs.
- Implement user authentication and saved locations.
- Expand forecast details with hourly updates.
- Integrate weather alerts and notifications.
- Develop a mobile-friendly progressive web app (PWA) version.
