"""
Week 5 Demo 2: read a text file

Purpose:
Show how a program can load stored text and display it.
"""

from pathlib import Path


input_file = Path(__file__).with_name("sample_note.txt")

with input_file.open("r", encoding="utf-8") as file:
    contents = file.read()

print("Loaded from:", input_file.name)
print(contents)

