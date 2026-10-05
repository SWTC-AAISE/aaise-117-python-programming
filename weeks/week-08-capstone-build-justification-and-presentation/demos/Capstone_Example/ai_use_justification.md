# Course Task Tracker - AI Use Justification

## Where AI Could Help

AI could help by:

* suggesting function organization
* identifying simple validation checks
* reviewing menu wording
* comparing whether features belong in the first version or backlog

---

## What the Student Must Govern

The student remains responsible for:

* choosing the project purpose
* deciding final scope
* understanding each function
* testing the program
* explaining why backlog features were deferred
* confirming that saved data behaves correctly

---

## What Was Accepted, Changed, or Rejected

Accepted:

* using a list of dictionaries for task data
* using JSON for simple persistence
* keeping validation checks small and readable

Changed:

* file persistence was added because a tracker should remember tasks between runs
* backlog features were kept out of the main build

Rejected:

* a class-based rewrite
* complex analytics
* deadline handling in the first version

---

## Why This Is Responsible AI Use

The AI-supported work stays inside the student's project intent. The code remains short enough to explain, and validation evidence is used instead of assuming the program is correct.

---

## AI-Assisted Revision: Internal Code Comments

The instructor requested internal comments for each function in the Python demo and an update to this justification. AI reviewed the existing code and added comments inside all 11 functions in `main.py`, explaining their purpose and selected decisions: input validation, default names, JSON persistence, completion status, and conversion from displayed task numbers to list indexes.

`validation_checks.py` defines no functions. AI added comments to its sample data, expected-result checks, and reporting loop instead. This revision changes comments and documentation only; it does not add features or change program behavior.

Accepted for this revision:

* concise comments tied to the existing code
* clarification that total planned minutes includes completed tasks
* explanations of empty-list and missing-file checks

The student must still compare each comment with the code and explain the functions in their own words. AI-generated comments support that review but do not demonstrate student understanding or establish that every possible input is handled.

Verification: the five existing validation checks passed after the comments were added. These checks cover total minutes, completion counts, empty lists, and a missing data file; they do not test every interactive menu path or file error.
