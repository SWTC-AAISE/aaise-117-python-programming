"""
Week 5 Demo 6: handling a missing file

Purpose:
Show a beginner-friendly file error example.
"""

from pathlib import Path


missing_file = Path(__file__).with_name("does_not_exist.txt")

try:
    with missing_file.open("r", encoding="utf-8") as file:
        print(file.read())
except FileNotFoundError:
    print("The file was not found:", missing_file.name)
    print("Create the file first or check the file path.")

