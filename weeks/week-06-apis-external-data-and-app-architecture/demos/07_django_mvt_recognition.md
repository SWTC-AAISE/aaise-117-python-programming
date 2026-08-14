# Week 6 Demo 7 - Django MVT Recognition Preview

This is a recognition-level walkthrough, not a full build target.

The purpose is to help students see where Python may live inside a larger web application.

## Core Idea

In a console script, one file often does almost everything:

* receives input
* stores values
* runs logic
* prints output

In a larger web application, those responsibilities are usually separated.

## Django MVT at a Beginner Level

### Model

Represents application data.

Example idea:

* a study task
* a course
* a due date
* a completion flag

### View

Handles the request and chooses what data should be prepared.

Example idea:

* get all study tasks
* filter incomplete tasks
* send them to a template

### Template

Displays information to the user.

Example idea:

* show a list of tasks in HTML
* show course names and due dates

### Form

Shapes and validates user input.

Example idea:

* require a task title
* require minutes to be a number
* reject missing fields

## Tiny Example Mapping

If a user submits a new study task:

1. The form checks the input.
2. The view decides what to do with the cleaned data.
3. The model represents or stores the task.
4. The template displays the result.

## Why This Matters

Students do not need to master Django here.

They do need to recognize that Python can move beyond console scripts into:

* request/response systems
* templates and forms
* structured application layers

That recognition helps later courses feel less abrupt.

