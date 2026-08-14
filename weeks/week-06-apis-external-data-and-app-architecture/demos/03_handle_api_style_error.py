"""
Week 6 Demo 3: handle an API-style error response

Purpose:
Show that external data may indicate failure even when JSON is valid.
"""

import json
from pathlib import Path


input_file = Path(__file__).with_name("simulated_error_response.json")

with input_file.open("r", encoding="utf-8") as file:
    response_data = json.load(file)

if response_data["status"] == "error":
    print("Request failed.")
    print("Message:", response_data["message"])
else:
    print("Request succeeded.")

