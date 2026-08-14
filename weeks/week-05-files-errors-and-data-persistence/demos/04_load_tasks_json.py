"""
Week 5 Demo 4: load structured data from JSON

Purpose:
Show how saved JSON data can be loaded and used meaningfully.
"""

import json
from pathlib import Path


input_file = Path(__file__).with_name("sample_tasks.json")

with input_file.open("r", encoding="utf-8") as file:
    tasks = json.load(file)

print("Loaded tasks from:", input_file.name)

for task in tasks:
    status = "done" if task["completed"] else "not done"
    print(task["course"], "-", task["task"], "-", task["minutes"], "minutes -", status)

