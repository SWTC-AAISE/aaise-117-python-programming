"""
Week 4 Demo 9: print debugging a grade summary

Purpose:
Show how print-debugging can help locate the first place where a value
becomes wrong.

Instructor note:
This demo intentionally contains a logic bug in the first version.
Do not reveal the fixed version too quickly. Let students compare expected
and actual output, then add the suggested print statements one at a time.
"""


students = [
    {"name": "Avery", "scores": [92, 88, 95]},
    {"name": "Blake", "scores": [70, 75, 80]},
    {"name": "Casey", "scores": [100, 90, 85]},
]


def summarize_grades_buggy(student_records):
    summaries = []

    running_total = 0

    for student in student_records:
        # Print-debugging checkpoint 1:
        # print("Starting student:", student["name"])
        # print("Running total at start:", running_total)

        for score in student["scores"]:
            running_total += score

            # Print-debugging checkpoint 2:
            # print("Added score:", score)
            # print("Running total now:", running_total)

        average = running_total / len(student["scores"])

        # Print-debugging checkpoint 3:
        # print("Calculated average:", average)

        summaries.append({
            "name": student["name"],
            "average": average,
        })

    return summaries


def summarize_grades_with_debug_output(student_records):
    summaries = []

    running_total = 0

    for student in student_records:
        print("\nStarting student:", student["name"])
        print("Running total at start:", running_total)

        for score in student["scores"]:
            running_total += score
            print("Added score:", score)
            print("Running total now:", running_total)

        average = running_total / len(student["scores"])
        print("Calculated average:", average)

        summaries.append({
            "name": student["name"],
            "average": average,
        })

    return summaries


def summarize_grades_fixed(student_records):
    summaries = []

    for student in student_records:
        student_total = 0

        for score in student["scores"]:
            student_total += score

        average = student_total / len(student["scores"])

        summaries.append({
            "name": student["name"],
            "average": average,
        })

    return summaries


print("BROKEN VERSION")
for summary in summarize_grades_buggy(students):
    print(summary["name"], "average:", summary["average"])

print("\nEXPECTED AVERAGES")
print("Avery: 91.66666666666667")
print("Blake: 75.0")
print("Casey: 91.66666666666667")

print("\nPROGRESSIVE PRINT-DEBUGGING VERSION")
summarize_grades_with_debug_output(students)

print("\nFIXED VERSION")
for summary in summarize_grades_fixed(students):
    print(summary["name"], "average:", summary["average"])

