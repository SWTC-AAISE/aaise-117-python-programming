"""
Week 5 Demo 7: handling invalid JSON

Purpose:
Show that file contents can exist but still fail to parse correctly.
"""

import json
from pathlib import Path


input_file = Path(__file__).with_name("sample_bad_tasks.json")

try:
    with input_file.open("r", encoding="utf-8") as file:
        data = json.load(file)

    print("Loaded", len(data), "records")
except json.JSONDecodeError as error:
    print("The JSON file could not be read correctly.")
    print("Problem file:", input_file.name)
    print("Error message:", error.msg)
    print("Line:", error.lineno, "Column:", error.colno)

