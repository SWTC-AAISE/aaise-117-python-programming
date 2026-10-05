"""
Simple validation checks for the Course Task Tracker capstone demo.
"""

from main import calculate_total_minutes, count_completed_tasks, load_tasks


# Use one completed and one incomplete task to check totals and completion counts.
sample_tasks = [
    {
        "course": "Python Programming",
        "task": "Finish validation checks",
        "minutes": 40,
        "complete": True,
    },
    {
        "course": "Math",
        "task": "Complete practice problems",
        "minutes": 35,
        "complete": False,
    },
]


# Each check pairs a function's actual result with an independently chosen expectation.
# Empty lists and a missing file cover basic boundary cases.
checks = [
    ("total minutes normal", calculate_total_minutes(sample_tasks), 75),
    ("total minutes empty", calculate_total_minutes([]), 0),
    ("completed count normal", count_completed_tasks(sample_tasks), 1),
    ("completed count empty", count_completed_tasks([]), 0),
    ("missing file loads empty list", load_tasks("missing_tasks_file.json"), []),
]


for label, actual, expected in checks:
    # Print the comparison so the presenter can review each result individually.
    print(label, "->", actual, "| expected:", expected, "| pass:", actual == expected)
