# Course Task Tracker

A working console demo of a completed capstone for **10-152-117 Python Programming**. The project follows the [Week 7 capstone proposal](../../Week_07_RBA_and_Project_Framing/05_capstone_proposal_example.md) and supports the Week 8 build justification and presentation activities.

## What the Application Does

Students can add assignment tasks for multiple courses, list tasks, mark tasks complete, and view a summary. The summary shows the number of tasks, the number completed, and total planned minutes across all tasks, including completed tasks.

Tasks are stored as a list of dictionaries and saved in `tasks.json`. The application loads this file at startup and saves after adding or marking a task complete and when choosing Save and exit. The included file provides sample data; changes made during a demo persist between runs.

## Requirements and Running

Install Python 3.6 or later. The project uses only Python's standard library; no additional packages are required.

Open a terminal in this `Capstone_Example` folder and run:

```powershell
python main.py
```

Choose an option from the menu:

1. List tasks
2. Add task
3. Mark task complete
4. Show summary
5. Save and exit

When adding a task, estimated minutes must be a whole number greater than zero. Blank course and task names receive default labels. To mark a task complete, enter its number from the displayed list.

The application locates `tasks.json` beside `main.py`. If that file is missing, the application starts with an empty task list and creates the file on the next save.

## Relationship Between the Python Files

The files are connected through a **one-way dependency**: `validation_checks.py` imports functions from `main.py`. The application does not import or require the validation script.

| File | Role | Uses the other file? |
| --- | --- | --- |
| `main.py` | Contains the application functions, menu, and JSON save/load logic | No; the tracker runs without `validation_checks.py` |
| `validation_checks.py` | Calls application functions with sample inputs and compares actual results with expected results | Yes; it imports three functions from `main.py` |

The validation script uses this import:

```python
from main import calculate_total_minutes, count_completed_tasks, load_tasks
```

It tests the actual application functions rather than maintaining separate copies of their logic. Keep both Python files in the same folder so the import can find `main.py`.

At the bottom of `main.py`, the following guard controls when the interactive application starts:

```python
if __name__ == "__main__":
    main()
```

When running `python main.py`, Python sets `__name__` to `"__main__"`, so the menu starts. When the validation script imports `main.py`, its module name is `"main"`, so the functions become available without starting the menu. Importing the application also does not load or save the task file, because those actions happen inside its functions.

## Running the Validation Checks

From this folder, run:

```powershell
python validation_checks.py
```

The script prints the actual result, expected result, and `pass: True` or `pass: False` for each check.

| Check | Expected Result |
| --- | --- |
| Total minutes for two sample tasks | `75` |
| Total minutes for an empty list | `0` |
| Completed count for the sample tasks | `1` |
| Completed count for an empty list | `0` |
| Loading `missing_tasks_file.json`, when absent | `[]` |

These checks use their own sample tasks and do not modify `tasks.json`. Review the printed comparisons: this simple script reports failures but does not use assertions or return a failing process exit code. Interactive input and save/reload behavior should also be demonstrated manually.

## Project Files

| File | Purpose |
| --- | --- |
| [main.py](main.py) | Runnable Course Task Tracker application with internal function comments |
| [validation_checks.py](validation_checks.py) | Five checks using imported application functions |
| [tasks.json](tasks.json) | Saved task data, initially populated with examples |
| [working_plan.md](working_plan.md) | Project scope, design, validation plan, and definition of done |
| [run_instructions.md](run_instructions.md) | Short instructions for running and evaluating the demo |
| [ai_use_justification.md](ai_use_justification.md) | AI assistance, human responsibilities, and the commenting revision |
| [presentation_outline.md](presentation_outline.md) | Suggested structure for the final presentation |

## Suggested Demonstration

1. Run the validation checks and review the five results.
2. Start the application and list the saved tasks.
3. Add a task, then mark that task complete.
4. Show the summary and explain how the totals are calculated.
5. Save and exit, then restart and confirm the changes remain.
6. Use the AI-use justification and presentation outline to discuss decisions and evidence.

## Scope and Limits

Deadlines, editing, deletion, and additional analytics remain backlog items. The first version focuses on lists, dictionaries, functions, loops, input validation, and JSON persistence.

The loader handles a missing file, invalid JSON, and a top-level value that is not a list. It assumes each saved task contains the expected fields and types; it does not validate every record or handle all operating-system file errors.
