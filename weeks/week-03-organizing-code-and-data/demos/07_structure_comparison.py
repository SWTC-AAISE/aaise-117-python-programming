"""
Week 3 Demo 7: rough vs organized structure

Purpose:
Compare a rough approach with a more organized function-based approach.

Instructor note:
Ask students which version is easier to change and why.
"""


def format_task(task_name, is_done):
    if is_done:
        status = "complete"
    else:
        status = "incomplete"
    return task_name + " - " + status


# Rough output without much structure.
print("ROUGH VERSION")
task_1 = "read"
task_1_done = True
print(task_1 + " - complete")

task_2 = "practice"
task_2_done = False
print(task_2 + " - incomplete")

print()
print("ORGANIZED VERSION")
print(format_task("read", True))
print(format_task("practice", False))

