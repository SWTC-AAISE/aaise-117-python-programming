"""
Week 5 Demo 8: data representation preview

Purpose:
Show that the same information can be represented in different structures.
"""


class StudyTask:
    def __init__(self, course, task, minutes):
        self.course = course
        self.task = task
        self.minutes = minutes


plain_text = "Python Programming | Review JSON notes | 25"
csv_style = "Python Programming,Review JSON notes,25"
dictionary_style = {
    "course": "Python Programming",
    "task": "Review JSON notes",
    "minutes": 25,
}
object_style = StudyTask("Python Programming", "Review JSON notes", 25)

print("PLAIN TEXT")
print(plain_text)

print("\nCSV STYLE")
print(csv_style)

print("\nDICTIONARY STYLE")
print(dictionary_style["course"], "-", dictionary_style["task"], "-", dictionary_style["minutes"])

print("\nOBJECT STYLE")
print(object_style.course, "-", object_style.task, "-", object_style.minutes)

