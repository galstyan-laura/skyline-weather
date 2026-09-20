# Skyline Weather — Real-Time Meteorological Intelligence Dashboard

<p align="center"><img src="docs/static/teaser/teaser.jpg" width="100%"/></p>

## Introduction

**Skyline Weather** is a modern, enterprise SaaS-style weather and atmospheric telemetry dashboard inspired by Ventusky and Apple Weather. Built with Python, Streamlit, and Plotly, the application is designed to deliver precise meteorological data visualizations, interactive hourly trends, and robust automated testing.

## Key Features

* **Interactive Hourly & 5-Day Forecast:** Dynamic charts displaying precise temperature curves, atmospheric conditions, and clean daily breakdown summaries.
* **Geospatial & Radar Visualization:** Real-time map rendering using Plotly geo-scatter components for targeted geographic intelligence.
* **Atmospheric Telemetry & Insights:** Advanced metrics tracking temperature deviations, wind vector dynamics, and thermal comfort indexes ("Feels Like").
* **Optimized Performance:** Efficient API integration with OpenWeatherMap utilizing data caching for smooth runtime transitions.
* **Robust Test Coverage:** Fully tested backend modules utilizing pytest and mock data streams to ensure application reliability.

## Tech Stack

* **Frontend & UI:** Streamlit (Custom Dark Theme CSS, Glassmorphism design system)
* **Data Visualization:** Plotly Express
* **Data Processing:** Pandas, Requests (OpenWeatherMap API)
* **Testing:** Pytest, Unittest.mock

## Setup & Installation

Follow these steps to set up and run the project locally:

* Clone the repository:

git clone [https://github.com/galstyan-laura/skyline-weather.git](https://github.com/galstyan-laura/skyline-weather.git)
cd skyline-weather

* Create and activate a virtual environment:

python -m venv .venv
.venv\Scripts\activate


* Install dependencies:


pip install -r requirements.txt


## Usage

**Run the application**
To start the Streamlit application locally, execute:

streamlit run app.py


**Running Tests**
To verify the application logic and run automated unit tests, use pytest:

pytest


**Author**
Laura Galstyan

Informatics and Applied Mathematics Student at Yerevan State University


**License**
Skyline Weather is open-source. Feel free to use and modify it for your projects.