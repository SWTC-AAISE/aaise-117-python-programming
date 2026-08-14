"""
Week 6 Demo 4: request-response flow

Purpose:
Show the thinking pattern behind API use even without making a live request.
"""


def build_request(city_name):
    return {
        "endpoint": "/weather",
        "query": {"city": city_name},
    }


def choose_display_values(response_data):
    current = response_data["current"]
    return {
        "temperature_f": current["temperature_f"],
        "condition": current["condition"],
    }


request_details = build_request("Sheboygan")
simulated_response = {
    "current": {
        "temperature_f": 61,
        "condition": "Partly Cloudy",
    }
}

selected_values = choose_display_values(simulated_response)

print("Request endpoint:", request_details["endpoint"])
print("Query city:", request_details["query"]["city"])
print("Selected values:", selected_values)

