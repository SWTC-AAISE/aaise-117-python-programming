"""
Week 6 Demo 6: console MVT-style preview

Purpose:
Show how a larger Python app may separate data, validation/input shaping,
logic, and display.
"""


def build_task_record(course, topic, minutes):
    return {
        "course": course,
        "topic": topic,
        "minutes": minutes,
    }


def validate_task_input(course, topic, minutes_text):
    if not course or not topic:
        return None, "Course and topic are required."

    minutes = int(minutes_text)
    return build_task_record(course, topic, minutes), None


def display_task(task_record):
    print("Course:", task_record["course"])
    print("Topic:", task_record["topic"])
    print("Minutes:", task_record["minutes"])


task, error = validate_task_input("Python Programming", "API practice", "30")

if error:
    print("Input error:", error)
else:
    display_task(task)

