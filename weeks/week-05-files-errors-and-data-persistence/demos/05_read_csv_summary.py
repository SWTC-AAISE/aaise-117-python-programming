"""
Week 5 Demo 5: read CSV data and summarize it

Purpose:
Show that structured flat data has fields that can be selected and summarized.
"""

import csv
from pathlib import Path


input_file = Path(__file__).with_name("sample_study_sessions.csv")

total_minutes = 0
completed_sessions = 0

with input_file.open("r", encoding="utf-8", newline="") as file:
    reader = csv.DictReader(file)

    for row in reader:
        minutes = int(row["minutes"])
        total_minutes += minutes

        if row["completed"] == "yes":
            completed_sessions += 1

        print(row["course"], "-", row["topic"], "-", minutes, "minutes")

print("Total minutes:", total_minutes)
print("Completed sessions:", completed_sessions)

