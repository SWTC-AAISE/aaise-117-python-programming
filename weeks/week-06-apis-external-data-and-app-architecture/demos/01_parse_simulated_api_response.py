"""
Week 6 Demo 1: parse a simulated API response

Purpose:
Show that API data usually arrives as structured JSON.
"""

import json
from pathlib import Path


input_file = Path(__file__).with_name("simulated_weather_response.json")

with input_file.open("r", encoding="utf-8") as file:
    response_data = json.load(file)

print("Location:", response_data["location"])
print("Condition:", response_data["current"]["condition"])
print("Temperature:", response_data["current"]["temperature_f"], "F")

