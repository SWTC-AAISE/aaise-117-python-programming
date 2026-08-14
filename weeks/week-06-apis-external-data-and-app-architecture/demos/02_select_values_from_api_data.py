"""
Week 6 Demo 2: select useful values from API-style data

Purpose:
Show that a program should choose useful fields rather than print raw JSON.
"""

import json
from pathlib import Path


input_file = Path(__file__).with_name("simulated_weather_response.json")

with input_file.open("r", encoding="utf-8") as file:
    response_data = json.load(file)

current = response_data["current"]
tomorrow = response_data["forecast"][1]

print("Weather summary for", response_data["location"])
print("Now:", current["temperature_f"], "F and", current["condition"])
print("Tomorrow high:", tomorrow["high_f"], "F")
print("Tomorrow low:", tomorrow["low_f"], "F")

