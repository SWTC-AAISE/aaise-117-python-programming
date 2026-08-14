"""
Week 4 Demo 7: function-based task tracker

Purpose:
Show the same idea organized with functions.
"""


def add_task(tasks, task_name):
    tasks.append(task_name)


def show_tasks(tasks):
    print("Tasks:")
    for task in tasks:
        print("-", task)


tasks = []
add_task(tasks, "read chapter")
add_task(tasks, "practice Python")
add_task(tasks, "submit assignment")
show_tasks(tasks)

