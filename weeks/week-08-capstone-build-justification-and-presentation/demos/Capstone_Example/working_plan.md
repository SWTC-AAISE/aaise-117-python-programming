# Course Task Tracker - Working Capstone Plan

## Source Proposal

This plan is based on:

`Week_07_RBA_and_Project_Framing/05_capstone_proposal_example.md`

## Project Purpose

Build a Python console app that helps a student track small assignment tasks for multiple courses.

The completed demo should show that the student can design, build, explain, test, and revise a realistic course-level Python project.

---

## Final Working Scope

The working version will include:

* add a task
* list current tasks
* mark a task complete
* show total planned minutes
* save tasks to a JSON file
* load tasks from a JSON file

These features match the original proposal while adding file persistence because a completed tracker should remember work between program runs.

---

## Deferred Backlog

These features are intentionally left out of the first completed version:

* task deadlines
* deleting tasks
* editing tasks
* external help file
* analytics beyond total planned minutes

They are useful, but they would increase the amount of branching, validation, and user-interface logic. The first version should stay explainable.

---

## Files to Include

* `main.py` - the main console app
* `tasks.json` - sample saved task data
* `validation_checks.py` - simple expected-vs-actual checks
* `run_instructions.md` - how to run and evaluate the demo
* `ai_use_justification.md` - how AI assistance is governed
* `presentation_outline.md` - short final presentation structure

---

## Main Data Structure

Tasks will be stored as a list of dictionaries.

Example:

```python
{
    "course": "Python Programming",
    "task": "Finish capstone validation notes",
    "minutes": 45,
    "complete": False
}
```

This structure is appropriate because it uses course-level concepts:

* lists
* dictionaries
* strings
* integers
* Booleans
* loops
* functions
* JSON file input/output

---

## Planned Functions

| Function | Responsibility |
| --- | --- |
| `load_tasks(filename)` | Read saved tasks from JSON or return an empty list |
| `save_tasks(filename, tasks)` | Write the current task list to JSON |
| `display_tasks(tasks)` | Print a readable task list |
| `add_task(tasks)` | Collect user input and append a new task |
| `mark_task_complete(tasks)` | Let the user choose an incomplete task and mark it complete |
| `calculate_total_minutes(tasks)` | Return the total planned minutes |
| `show_summary(tasks)` | Display task count, completion count, and total minutes |
| `get_positive_integer(prompt)` | Validate numeric input |
| `main()` | Run the menu loop |

---

## User Flow

1. Program starts.
2. Program loads `tasks.json`.
3. User sees a menu.
4. User chooses one action.
5. Program performs the action and shows a message.
6. Program saves task data after changes.
7. User exits when finished.

---

## Validation Plan

Validation should focus on behavior a user would notice:

* total planned minutes is calculated correctly
* completed tasks are counted correctly
* empty task lists do not crash the summary
* invalid saved files do not crash the program
* task completion changes only the selected task

The demo includes `validation_checks.py` so the instructor can see simple evidence without needing a full testing framework.

---

## Reality Contact Decision

The completed demo adds save/load behavior and leaves edit/delete/deadline features out.

This is a strong revision because:

* save/load behavior makes the project feel complete
* the code remains short enough to explain
* the core proposal features are still present
* the backlog remains available for future improvement

---

## Definition of Done

The project is complete when:

* `python main.py` starts the menu without errors
* sample tasks load from `tasks.json`
* a user can add a task
* a user can mark a task complete
* the task list displays readable information
* the summary shows total planned minutes
* task changes are saved
* `python validation_checks.py` prints passing checks
* the student can explain where AI helped and where human decisions governed the work

