"""
Week 3 Demo 5: dictionary lookup

Purpose:
Show that a dictionary stores values by key.

Instructor note:
Connect this to real-world lookup behavior: label -> value.
"""

course = {
    "number": "10-152-117",
    "title": "Python Programming",
    "credits": 2,
}

print("Course number:", course["number"])
print("Course title:", course["title"])
print("Credits:", course["credits"])

course["meeting_days"] = "Monday, Tuesday, Thursday"

print("Meeting days:", course["meeting_days"])

