"""
Week 4 Demo 8: class-based task tracker

Purpose:
Show a simple class-based version for recognition and interpretation.

Instructor note:
Do not turn this into deep OOP theory. Keep the language plain:
the object stores tasks, and methods are actions the object can do.
"""


class TaskTracker:
    def __init__(self):
        self.tasks = []

    def add_task(self, task_name):
        self.tasks.append(task_name)

    def show_tasks(self):
        print("Tasks:")
        for task in self.tasks:
            print("-", task)


tracker = TaskTracker()
tracker.add_task("read chapter")
tracker.add_task("practice Python")
tracker.add_task("submit assignment")
tracker.show_tasks()

