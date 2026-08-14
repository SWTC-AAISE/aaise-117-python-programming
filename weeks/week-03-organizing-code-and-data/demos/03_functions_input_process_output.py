"""
Week 3 Demo 3: separating input, processing, and output

Purpose:
Show that functions can separate responsibilities in a small program.

Instructor note:
This version uses hardcoded values so the focus stays on structure.
"""


def calculate_average(score_1, score_2, score_3):
    total = score_1 + score_2 + score_3
    average = total / 3
    return average


def get_status(average):
    if average >= 70:
        return "passing"
    return "not passing"


def show_result(student_name, average, status):
    print("Student:", student_name)
    print("Average:", average)
    print("Status:", status)


name = "Morgan"
average_score = calculate_average(82, 74, 91)
student_status = get_status(average_score)
show_result(name, average_score, student_status)

