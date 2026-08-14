"""
Week 6 Demo 9: environment-based fallback preview

Purpose:
Introduce the idea that code may use fallback data in development and
live integrations in production.

Instructor note:
This is recognition-level only. It is meant to show the concept of
conditional behavior by environment, not to teach deployment engineering.
"""

import json
import os
from pathlib import Path


def load_live_api_data():
    # In a real project, this function would call the real API.
    return {
        "source": "live API",
        "location": "Sheboygan",
        "current": {
            "temperature_f": 61,
            "condition": "Partly Cloudy",
        },
    }


def load_fallback_data():
    fallback_file = Path(__file__).with_name("simulated_weather_response.json")

    with fallback_file.open("r", encoding="utf-8") as file:
        fallback_data = json.load(file)

    fallback_data["source"] = "simulated JSON fallback"
    return fallback_data


environment = os.getenv("APP_ENV", "DEVELOPMENT").upper()

if environment == "PRODUCTION":
    api_data = load_live_api_data()
else:
    api_data = load_fallback_data()

print("Environment:", environment)
print("Data source:", api_data["source"])
print("Location:", api_data["location"])
print("Temperature:", api_data["current"]["temperature_f"], "F")
print("Condition:", api_data["current"]["condition"])

