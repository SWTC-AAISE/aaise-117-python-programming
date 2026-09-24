# One Study Task Through MVT

## A valid request

1. The user opens `/add/`. `tasks/urls.py` sends that request to
   `add_task` in `tasks/views.py`.
2. `add_task` creates an empty `StudyTaskForm` and renders
   `tasks/templates/tasks/task_form.html`. The template displays the fields
   and a Save task button.
3. The user submits `Python Programming`, `Review functions`, and `30`.
   The browser sends a POST request to `/add/`.
4. The same view creates `StudyTaskForm(request.POST)` and calls
   `form.is_valid()`. `tasks/forms.py` names the fields; Django checks that
   required text is present and that estimated minutes is a nonnegative
   integer.
5. On success, `form.save()` creates a `StudyTask` as defined in
   `tasks/models.py`, stored in the local SQLite database. The view redirects
   to `/`.
6. The `/` route calls `task_list`. That view queries `StudyTask` records
   and passes them to `tasks/templates/tasks/task_list.html`, which displays
   each task in HTML.

## An invalid request

If estimated minutes is `not-a-number`, `form.is_valid()` is false. The view
does not call `form.save()`. It renders `task_form.html` again with the bound
form and its error. No task is added to the list.

## What the names mean

| Part | In this app | Job |
| --- | --- | --- |
| Model | `tasks/models.py` | Defines the study-task data that Django stores. |
| View | `tasks/views.py` | Handles requests, chooses actions, and supplies data to templates. |
| Template | `task_form.html`, `task_list.html` | Displays HTML to the user. |
| Form | `tasks/forms.py` | Defines input fields and supports validation. |
| URL routing | `tasks/urls.py` | Connects a web address to a view. |

Forms and URL routing support the flow; they are not the M, V, or T in MVT.
The `site_config/` files start Django and are outside this assignment's
reading target.

## Console comparison

In a console program, `input()` may collect a value and `print()` may show
the result in one running script. Here, a browser sends a request; a view
responds to that request, a form validates input, a model stores data, and a
template renders the response. The same study-task idea has a different flow.
