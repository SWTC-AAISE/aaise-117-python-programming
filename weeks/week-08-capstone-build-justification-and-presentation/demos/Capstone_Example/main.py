"""
Course Task Tracker

A small console capstone demo for 10-152-117 Python Programming.
"""

import json
from pathlib import Path


DATA_FILE = Path(__file__).with_name("tasks.json")


def load_tasks(filename):
    # Read saved tasks; a missing file means this is a new task list.
    path = Path(filename)

    if not path.exists():
        return []

    # Handle invalid JSON and reject a top-level value that is not a list.
    try:
        with path.open("r", encoding="utf-8") as file:
            tasks = json.load(file)
    except json.JSONDecodeError:
        print("The task file could not be read. Starting with an empty task list.")
        return []

    if not isinstance(tasks, list):
        print("The task file format was not valid. Starting with an empty task list.")
        return []

    return tasks


def save_tasks(filename, tasks):
    # Replace the saved file with the current list in readable JSON format.
    path = Path(filename)

    with path.open("w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=2)


def get_positive_integer(prompt):
    # Keep prompting until the user supplies a whole number greater than zero.
    while True:
        user_input = input(prompt).strip()

        if user_input.isdigit() and int(user_input) > 0:
            return int(user_input)

        print("Please enter a whole number greater than 0.")


def display_tasks(tasks):
    # Show an empty-list message or a numbered list with each task's status.
    if len(tasks) == 0:
        print("No tasks have been added yet.")
        return

    print()
    print("Current Tasks")
    print("-" * 40)

    for index, task in enumerate(tasks, start=1):
        status = "complete" if task["complete"] else "in progress"
        print(f"{index}. [{status}] {task['course']} - {task['task']} ({task['minutes']} min)")


def add_task(tasks):
    # Collect task details and validate the estimated time with the shared helper.
    course = input("Course name: ").strip()
    task_name = input("Task name: ").strip()
    minutes = get_positive_integer("Estimated minutes: ")

    # Supply default labels when the user leaves either name blank.
    if course == "":
        course = "Unlisted Course"

    if task_name == "":
        task_name = "Untitled Task"

    # New tasks start incomplete; append updates the caller's task list.
    task = {
        "course": course,
        "task": task_name,
        "minutes": minutes,
        "complete": False,
    }

    tasks.append(task)
    print("Task added.")


def mark_task_complete(tasks):
    # Let the user select a displayed task, checking that the selection exists.
    if len(tasks) == 0:
        print("There are no tasks to complete.")
        return

    display_tasks(tasks)
    task_number = get_positive_integer("Task number to mark complete: ")

    if task_number < 1 or task_number > len(tasks):
        print("That task number was not found.")
        return

    # Display numbers start at 1, while Python list indexes start at 0.
    tasks[task_number - 1]["complete"] = True
    print("Task marked complete.")


def calculate_total_minutes(tasks):
    # Add estimates for all tasks, including those already completed.
    total = 0

    for task in tasks:
        total += task["minutes"]

    return total


def count_completed_tasks(tasks):
    # Count only tasks whose completion flag is true; an empty list returns 0.
    completed = 0

    for task in tasks:
        if task["complete"]:
            completed += 1

    return completed


def show_summary(tasks):
    # Use the calculation helpers to display task counts and planned time.
    total_tasks = len(tasks)
    completed_tasks = count_completed_tasks(tasks)
    total_minutes = calculate_total_minutes(tasks)

    print()
    print("Summary")
    print("-" * 40)
    print(f"Tasks planned: {total_tasks}")
    print(f"Tasks complete: {completed_tasks}")
    print(f"Total planned minutes: {total_minutes}")


def show_menu():
    # Display the same numbered choices on each pass through the menu loop.
    print()
    print("Course Task Tracker")
    print("1. List tasks")
    print("2. Add task")
    print("3. Mark task complete")
    print("4. Show summary")
    print("5. Save and exit")


def main():
    # Load tasks once, then route each menu choice to its corresponding function.
    tasks = load_tasks(DATA_FILE)

    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            display_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
            # Save after changes so they persist even before the user exits.
            save_tasks(DATA_FILE, tasks)
        elif choice == "3":
            mark_task_complete(tasks)
            save_tasks(DATA_FILE, tasks)
        elif choice == "4":
            show_summary(tasks)
        elif choice == "5":
            save_tasks(DATA_FILE, tasks)
            print("Tasks saved. Goodbye.")
            break
        else:
            print("Please choose a menu option from 1 to 5.")


if __name__ == "__main__":
    main()
