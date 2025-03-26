# Weather Web Application

## Distinctiveness and complexity requirements

> *Your web application must be sufficiently distinct from the other projects in this course and more complex than those.*

This project does not contain the same structure as other projects like a social network, email client, auction site, or search engine. It is a weather client that has user accounts associated to locations. In addition to those features it provides users with information from a live API and it makes use of the API to graphically display the weather conditions around the user. It also provides relevant precipitation information on a timeline to make it more convenient to users in rainier locations such as Seattle.

> *A project that appears to be a social network is a priori deemed by the staff to be indistinct from Project 4, and should not be submitted; it will be rejected.*

Ideas from the course such as user accounts and their creation and administration were used. Only ideas and topics that spanned the entirety of the course were considered when making the application. The aggregated skills that this course provides are what I used to construct the application and it deals with a different kind of user manipulable data (weather) than the other projects in the course.

> *A project that appears to be an e-commerce site is strongly suspected to be indistinct from Project 2, and your `README.md` file should be very clear as to why it’s not. Failing that, it should not be submitted; it will be rejected.*

This project is a weather application and not an e-commerce website. The purpose of this website is to display certain aspects of the weather that is local to a user. You can find below a feature by feature description of the application and its uses.

## Overview

This weather application provides users with a comprehensive and interactive weather monitoring experience. By combining real-time weather data with dynamic mapping capabilities, users can visualize current weather conditions and forecasts in an intuitive interface. The application serves as a powerful tool for both casual users seeking daily weather updates and those requiring more detailed meteorological information.

## Core Features

### Real-Time Weather Display
The current weather display serves as the application's primary information hub, providing users with comprehensive meteorological data for their selected location. The interface presents temperature readings in Celsius, accompanied by descriptive weather icons that visually represent current conditions. Beyond basic temperature readings, the display includes critical atmospheric metrics such as humidity percentages and wind speed measurements in meters per second. The "feels like" temperature feature accounts for humidity and wind factors, giving users a more accurate sense of outdoor conditions. All this information is organized in a clean, card-based layout with clear typography and intuitive iconography, making it easy for users to quickly grasp current weather conditions at a glance. The data updates in real-time, ensuring users always have access to the most current weather information.

### Interactive Weather Map
The map interface represents the application's most sophisticated feature, powered by Leaflet.js for smooth and responsive interaction. Users can seamlessly switch between detailed street maps and high-resolution satellite imagery, providing context for weather patterns. The map supports multiple weather overlay layers, including precipitation, cloud coverage, temperature distributions, and wind patterns, all of which can be toggled independently or combined for comprehensive weather analysis. A standout feature is the custom opacity control, allowing users to fine-tune the visibility of weather layers for optimal visualization. The map includes a location marker system that precisely pinpoints selected areas, while the layer control panel provides easy access to all available map options. The interface is optimized for both mouse and touch interactions, ensuring smooth operation across all devices. Weather layers are color-coded and updated regularly to reflect current conditions, making it easy to track weather patterns and movements.

### Precipitation Timeline
The precipitation timeline feature offers an innovative approach to weather forecasting, displaying an 8-hour prediction window through an intuitive visual interface. Each hour segment is represented by a dynamic bar graph that indicates precipitation probability through both height and color intensity. The timeline includes detailed temperature readings for each hour, accompanied by weather condition icons that provide immediate visual feedback about expected conditions. Time stamps are clearly displayed for each segment, helping users plan their activities with precision. The probability bars use a gradient color scheme that makes it easy to identify periods of higher precipitation likelihood, while the compact design ensures all critical information is visible without overwhelming the user. The timeline's responsive design automatically adjusts to different screen sizes while maintaining clarity and usability, with special consideration given to mobile viewing scenarios where space is at a premium.

### Responsive Design System
The application's responsive design system goes beyond basic mobile compatibility, implementing a sophisticated approach to content presentation across different devices and orientations. On desktop displays, the interface takes full advantage of available screen real estate, presenting an expanded map view alongside detailed weather information and the full precipitation timeline. Tablet users experience a carefully optimized layout that maintains full functionality while adjusting component sizes and positioning for touch interaction. The mobile interface completely reorganizes content for vertical scrolling, with a collapsible map view and streamlined controls designed specifically for smaller screens. The design system includes specific optimizations for landscape orientation, particularly useful for map viewing on mobile devices. Special attention has been paid to touch targets and interactive elements, ensuring they remain accessible and functional across all device sizes. The system also includes performance optimizations for different devices, ensuring smooth operation regardless of screen size or device capabilities.

## Technical Implementation

Built on the Django framework, the application integrates seamlessly with the OpenWeatherMap API to fetch real-time weather data. The frontend utilizes Bootstrap for responsive styling, ensuring a consistent experience across desktop and mobile devices. The mapping functionality leverages Leaflet.js for smooth, interactive map operations and weather layer visualization.

## Setup and Installation

### Prerequisites
- Python 3.x
- pip (Python package installer)
- Git

### Installation Steps

1. Clone the repository
```bash
git clone [your-repository-url]
cd weather-webapp
