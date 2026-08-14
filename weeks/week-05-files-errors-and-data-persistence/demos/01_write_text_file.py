"""
Week 5 Demo 1: write a text file

Purpose:
Show the basic idea of saving information to a file.
"""

from pathlib import Path


output_file = Path(__file__).with_name("demo_output_note.txt")

message_lines = [
    "StudyPilot Notes",
    "----------------",
    "1. Review Python examples",
    "2. Practice debugging carefully",
    "3. Prepare for the next lab",
]

with output_file.open("w", encoding="utf-8") as file:
    for line in message_lines:
        file.write(line + "\n")

print("Wrote file:", output_file.name)

