# Weather Web Application

## Distinctiveness and Complexity

Delivering pizza on a bike requires efficiency, adaptability, and precision, especially in a city like Seattle, where the weather can change rapidly. A sudden downpour or high winds can significantly affect delivery speed and safety, making real-time weather awareness essential. Standard weather applications provide general forecasts, but they often lack the precision and responsiveness necessary for cyclists making quick, informed route decisions. Recognizing this need, I developed this **Weather Web Application**, designed to help riders **plan efficiently, avoid delays, and optimize their time on the road**.

Unlike conventional weather tools, this application **transforms raw forecasts into actionable insights**. The **precipitation timeline** is a crucial feature that offers an **hourly breakdown of rain intensity**, helping users anticipate conditions rather than react to them. The **interactive weather map** displays temperature shifts, wind speeds, and cloud coverage, ensuring riders can assess patterns visually rather than relying solely on numbers. This level of **real-time visualization** allows cyclists to make immediate adjustments to their delivery schedule and **choose optimal routes** based on actual conditions.

A key aspect of the project’s **distinctiveness** lies in its **personalized weather tracking** capabilities. By linking **user accounts to specific locations**, the application ensures that weather updates remain **relevant to a cyclist’s exact delivery area**, eliminating the need for repeated manual searches. Data retrieval from the **OpenWeatherMap API** ensures information remains accurate and **continuously updated**. The interface, built with **Bootstrap for responsiveness**, adapts seamlessly to different devices, allowing cyclists to **quickly check conditions mid-route**.

This project is **not merely a variation of standard coursework** but a **practical tool that fills a real-world gap**. It integrates **real-time data, interactive maps, and location-based forecasting**—none of which were the primary focus of previous projects. The technical depth required for **API integration, mapping overlays, and user data management** within Django presented significant challenges, making this an **advanced and rewarding application to build**.

Ultimately, this application serves as **more than just a weather app**—it is a **decision-making tool for urban cyclists**, enabling them to **minimize downtime, improve efficiency, and make smarter delivery choices**. Its **unique combination of interactive weather tracking, cyclist-focused features, and real-time updates** ensures that it stands apart both as a technical achievement and as a **practical aid for navigating city streets**.

---

## Project Structure

This application is organized into several components, each responsible for handling different aspects of weather tracking and user interaction.

The main Django project directory, `weather/`, contains configuration files managing the framework's core functionality. The `settings.py` file defines database configurations, installed applications, middleware, and static file locations. The `urls.py` file determines how user requests are routed, connecting them to specific views. The `wsgi.py` and `asgi.py` files are entry points for different deployment models, ensuring compatibility with both standard and asynchronous requests.

Within the `weather_app/` directory, the **core application logic** is implemented. The `models.py` file structures database entries, defining user accounts and location tracking features. The `views.py` file contains functions responsible for fetching weather data, rendering templates, and handling user interactions. The `urls.py` file manages the application’s specific routes, ensuring that different sections (such as the map interface or user settings) are properly linked.

Additional files such as `forms.py` manage user input, streamlining location selection and profile settings. The `admin.py` file allows for backend management, making it possible to modify accounts and weather preferences through Django’s built-in administrative interface. The `migrations/` directory holds database schema changes, ensuring version control as the application evolves.

Frontend elements are stored in `templates/weather_app/`, where HTML files dynamically render weather conditions, mapping features, and interactive timelines. The `static/` folder contains styling and JavaScript logic, improving usability across different devices. Specifically, `map.js` enables Leaflet.js functionality, ensuring smooth weather layer rendering and real-time map updates.

Other essential files include `.env`, which securely stores API keys and sensitive credentials, and `requirements.txt`, listing dependencies needed for installation. The SQLite database (`db.sqlite3`) maintains stored user preferences and historical weather data, ensuring continuity between sessions.

---

## How to Run the Application

### Prerequisites

Before running the application, ensure the following dependencies are installed:

- **Python 3.x**
- **Django**
- **Bootstrap**
- **Leaflet.js**
- **OpenWeatherMap API key**

### Installation Steps

1. Clone the repository and navigate to the project directory:
   ```bash
   git clone https://github.com/JPBradley3/Weather-App
   cd weather-webapp

