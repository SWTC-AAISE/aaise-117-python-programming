# Study Task MVT Example (Assignment 12)

This small Django app exists for architecture inspection. It has one model,
one input form, two view functions, two routes, and two templates. A student
can complete Assignment 12 by reading these files and the trace guide; running
the app is optional.

## Inspect first

1. `tasks/templates/tasks/task_form.html` receives a task through an HTML form.
2. `tasks/urls.py` connects `/add/` to `tasks/views.py:add_task`.
3. `tasks/forms.py:StudyTaskForm` checks the submitted fields.
4. `tasks/models.py:StudyTask` defines the stored record.
5. `tasks/views.py:add_task` saves valid input and redirects to the list.
6. `tasks/views.py:task_list` supplies records to
   `tasks/templates/tasks/task_list.html` for display.

Read `MVT_TRACE.md` for a complete valid and invalid request path, then use
`ASSIGNMENT_12_WORKSHEET.md` for the student response.

## Run locally (instructor or optional exploration)

From this folder:

```powershell
python -m venv .venv
.\.venv\Scripts\python.exe -m pip install django
.\.venv\Scripts\python.exe manage.py migrate
.\.venv\Scripts\python.exe manage.py runserver
```

These commands use the virtual environment directly, so activation is not
required in PowerShell.

Open `http://127.0.0.1:8000/`, then choose **Add a task**. Try
`Python Programming`, `Review functions`, and `30`. The saved task appears on
the list page. For an invalid example, enter `not-a-number` for estimated
minutes; the form should stay on screen and show a validation error.

`db.sqlite3` is created locally after migration and is not part of the
student reading set. `site_config/settings.py` and `manage.py` are only the
minimum Django setup needed to run the example. They are not Assignment 12
inspection targets.

This is a local classroom demo, not a deployment template.
