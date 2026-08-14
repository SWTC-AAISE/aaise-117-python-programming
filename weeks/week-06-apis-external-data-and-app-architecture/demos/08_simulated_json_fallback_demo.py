"""
Week 6 Demo 8: simulated JSON fallback

Purpose:
Make the fallback concept explicit.

Instructor note:
This demo shows that when a live API is unavailable, unstable, or not the
main lesson target, a local simulated JSON file can be used to keep the focus
on reading structure, selecting values, and validating logic.
"""

import json
from pathlib import Path


def load_api_style_data(live_available):
    if live_available:
        # In a real application, this branch could make a network request.
        return {
            "source": "live API",
            "location": "Sheboygan",
            "current": {
                "temperature_f": 61,
                "condition": "Partly Cloudy",
            },
        }

    fallback_file = Path(__file__).with_name("simulated_weather_response.json")

    with fallback_file.open("r", encoding="utf-8") as file:
        fallback_data = json.load(file)

    fallback_data["source"] = "simulated JSON fallback"
    return fallback_data


api_data = load_api_style_data(live_available=False)

print("Data source:", api_data["source"])
print("Location:", api_data["location"])
print("Temperature:", api_data["current"]["temperature_f"], "F")
print("Condition:", api_data["current"]["condition"])

print("\nTeaching point:")
print("The lesson target is reading and using the JSON structure correctly,")
print("not proving that the internet worked during class.")

