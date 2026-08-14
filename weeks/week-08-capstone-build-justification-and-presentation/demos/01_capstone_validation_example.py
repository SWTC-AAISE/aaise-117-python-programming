"""
Week 8 Demo 1: capstone validation example

Purpose:
Show a small example of validation evidence for an explainable capstone.
"""


def calculate_completion_rate(completed_tasks, total_tasks):
    if total_tasks == 0:
        return 0

    return completed_tasks / total_tasks


def study_goal_status(total_minutes, goal_minutes):
    if total_minutes >= goal_minutes:
        return "goal met"
    return "goal not met"


checks = [
    ("completion rate normal", calculate_completion_rate(3, 5), 0.6),
    ("completion rate zero total", calculate_completion_rate(0, 0), 0),
    ("goal met case", study_goal_status(120, 100), "goal met"),
    ("goal not met case", study_goal_status(45, 100), "goal not met"),
]

for label, actual, expected in checks:
    print(label, "->", actual, "| expected:", expected, "| pass:", actual == expected)

