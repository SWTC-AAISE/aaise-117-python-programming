# Week 7 Demo 4 - AI Boundary Example

## Good AI Roles

AI may help with:

* drafting a first function
* suggesting alternate organization
* identifying possible edge cases
* rewriting unclear output messages
* comparing two code structures

---

## Human-Governed Decisions

The student should still decide:

* what the project is for
* what features are required
* whether the scope is realistic
* what data matters
* whether generated code is correct
* what should be changed or rejected

---

## Sample GitHub Copilot Prompts for VS Code

Use these prompts after defining the project's purpose, scope, and likely structure.

### AI-Assisted Prompts

> In this Python file, explain the current program structure. Identify which functions handle input, process data, and display output. Do not rewrite the code yet.

> Review my beginner-level Python task tracker and list possible edge cases I should test. Focus on input validation, empty task lists, and marking tasks complete. Do not add new features.

> Compare these two possible structures for my small console app: a single script with functions, or a list of dictionaries with separate helper functions. Explain the tradeoffs for a beginner project without choosing the project's scope for me.

### AI-Enabled Crossover Prompt

> Using the behavior I already described in my comments, draft one beginner-readable Python function that totals planned minutes from a list of task dictionaries. Keep it small, use concepts from this course, and explain any assumptions you make.

The first three prompts ask Copilot to explain, review, or compare while you the developer, make the decisions. The final prompt allows Copilot to generate one bounded piece of code that you must review and test.

---

## Teaching/Learning Point

AI can assist implementation.

AI should not quietly become the owner of project purpose, scope, or validation.

