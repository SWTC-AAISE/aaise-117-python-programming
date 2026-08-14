"""
Week 5 Demo 3: save structured data as JSON

Purpose:
Show how Python collections can be saved in a structured file format.
"""

import json
from pathlib import Path


tasks = [
    {"task": "Read chapter", "minutes": 20, "completed": True},
    {"task": "Practice loops", "minutes": 35, "completed": False},
    {"task": "Review notes", "minutes": 15, "completed": False},
]

output_file = Path(__file__).with_name("demo_saved_tasks.json")

with output_file.open("w", encoding="utf-8") as file:
    json.dump(tasks, file, indent=2)

print("Saved JSON file:", output_file.name)

