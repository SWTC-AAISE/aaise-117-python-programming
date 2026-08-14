"""
Week 3 Demo 6: list of dictionaries

Purpose:
Show a common beginner-friendly structure for multiple records.

Instructor note:
This prepares students for later JSON and API response structures.
"""

students = [
    {"name": "Avery", "score": 92},
    {"name": "Blake", "score": 76},
    {"name": "Casey", "score": 64},
]

for student in students:
    if student["score"] >= 70:
        status = "passing"
    else:
        status = "not passing"

    print(student["name"], "-", student["score"], "-", status)

