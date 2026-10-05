# Suggested AI Prompt: Plan One Backlog Feature

## Purpose and AI Mode

Use this prompt to plan one extension to the Course Task Tracker in **AI-Assisted mode**. AI explains, compares approaches, and suggests validation steps. The student chooses the scope, writes the implementation, tests it, and explains the result. This activity requests plain-language guidance only, with no code or pseudocode.

This boundary follows the [Week 7 AI boundary examples](../../Week_07_RBA_and_Project_Framing/04_ai_boundary_example.md) and the [Python AI Use Addendum](../../../Python_AI_Use_Addendum.md). Assignment-specific instructions still apply.

## Before Using the Prompt

1. Choose one feature from the table below.
2. Replace the bracketed placeholders in the prompt with your own intent and decisions.
3. Provide your current `main.py`, `validation_checks.py`, `tasks.json`, and `README.md` as context. Include `working_plan.md` if available. In an editor-based AI tool, explicitly include those files in the conversation context; otherwise attach or paste their contents. Use your current version if you have already completed another extension.
4. Read the resulting plan, resolve open decisions, and implement the selected feature yourself.
5. Test and document that feature before using the prompt again for another backlog item.

| Feature | Decide Before Planning |
| --- | --- |
| Task deadlines | Are deadlines optional? What date format should users enter? Is the goal to display deadlines, or also identify overdue tasks? |
| Delete a task | Should deletion require confirmation? What should cancellation do? |
| Edit a task | Which fields may change? How should a user keep an existing value? |
| Display help from a text file | What should the help explain? What should happen when the help file is missing? |
| Additional summary analytics | Choose one specific measure, such as remaining planned minutes or completion percentage. Define what it means. |

The original proposal lists deadlines, deletion, editing, and file-based help. Additional analytics appears in the completed demo's working-plan backlog. Select it only if it fits your approved project scope.

## Student Prompt

Copy the following prompt into your AI conversation after filling in the placeholders:

> You are my planning tutor for the Course Task Tracker capstone in 10-152-117 Python Programming. Work in AI-Assisted mode: provide explanations, comparisons, and a detailed plain-language plan while I make the decisions and write the implementation.
>
> **My intent and selected scope**
>
> - Selected backlog feature: [choose exactly one feature].
> - User need: [explain who needs this feature and why].
> - Desired behavior: [describe what the user should be able to do and see].
> - My decisions so far: [state relevant choices from the feature table, or identify what is undecided].
> - Features I have already implemented: [list them, or say none].
> - Course concepts and constraints: [describe what I know and any assignment limits].
>
> **Current project context**
>
> Review the files I have supplied before giving project-specific advice. If a required file is unavailable, say which one and ask me to provide it. Do not claim to have inspected files you cannot access.
>
> The baseline tracker is a console application that adds tasks, lists tasks, marks tasks complete, and summarizes task counts and total planned minutes. It uses a list of dictionaries with course, task, minutes, and complete fields. It loads and saves tasks in a JSON file. Confirm these details against my current files, since my version may have changed.
>
> The application lives in main.py. The validation script imports calculate_total_minutes, count_completed_tasks, and load_tasks from main.py. The application does not depend on the validation script. Its main-module guard prevents the menu from opening when its functions are imported. Preserve this relationship when planning new checks.
>
> **Boundaries for your response**
>
> - Plan only my selected feature. If I name multiple features, ask me to choose one before planning.
> - Do not generate Python code, pseudocode, replacement files, patches, executable commands, or implementation snippets. Do not edit files or run tools that modify the project.
> - Use ordinary sentences, numbered steps, and tables. You may name files, existing functions, proposed function responsibilities, and data fields without giving implementation syntax or line-by-line instructions that amount to pseudocode.
> - Keep the design appropriate for a beginner console project using the existing structure and standard library. Explain any new concept needed for the selected feature. Avoid adding frameworks or rewriting the application architecture.
> - Leave final scope and design choices to me. Compare meaningful alternatives, explain tradeoffs, and label recommendations and assumptions clearly.
> - Ask up to three focused questions if unanswered decisions would materially change the plan. Wait for my answers before finalizing those dependent steps. For minor details, provide a labeled assumption for me to review.
> - Do not treat a proposed plan or suggested tests as proof that the feature works. Do not invent test results or claim I have completed work.
>
> **Provide the following planning sections**
>
> 1. Intent and success criteria: restate my selected feature and give observable acceptance criteria. Identify any decisions I still need to make.
> 2. Current behavior and impact: explain which existing functions and files are relevant, what they do now, and what responsibilities need to change. Distinguish confirmed observations from assumptions.
> 3. Data and persistence: explain whether the selected feature needs new fields or files. Describe how existing saved tasks will continue to work, how defaults should behave, and how changes will survive a save and reload. If the feature needs no data change, explain why.
> 4. User interaction: describe the menu change, prompts, outputs, validation messages, cancellation behavior where relevant, and empty-list behavior. Explain how displayed task numbers should be interpreted after changes to the list.
> 5. Ordered implementation plan: give small, manageable steps in dependency order. For each step, identify the file or function responsibility involved, explain the purpose of the change, and describe an observable checkpoint I can use after writing it. Include the reasoning I need to implement the step myself, without code or pseudocode.
> 6. Validation plan: provide a table with the scenario, sample input or starting state, expected observable result, and whether I should check it manually or through a function check in validation_checks.py. Include normal use, invalid input, empty or boundary cases, and persistence when relevant. Explain which checks can import functions without starting the menu and which require interactive testing. The existing script prints comparisons; a successful process exit alone does not prove those comparisons passed.
> 7. Regression checks: describe how I should verify that adding, listing, marking complete, summarizing, and saving/loading still work. Keep total planned minutes defined as the sum of estimates for all tasks, including completed tasks. Discuss existing validation expectations that should stay the same or legitimately change.
> 8. Documentation and AI-use evidence: identify what I should update in README.md, run_instructions.md, working_plan.md, and ai_use_justification.md as appropriate. Give questions for recording my intent, AI suggestions, what I accepted/changed/rejected, decisions I made, and actual test evidence. Do not write a completed justification or personal reflection on my behalf.
> 9. Understanding checkpoint and definition of done: ask questions I should be able to answer about data flow, function responsibilities, edge cases, and testing. Finish with a checklist of evidence I should collect before calling this feature complete.
>
> **Apply only the considerations relevant to my chosen feature**
>
> - Deadlines: discuss a clear date format, valid calendar dates, optional values, tasks saved before deadline fields existed, and display behavior. Add overdue classification only if I selected it, and clarify whether completed tasks can count as overdue.
> - Deletion: discuss selecting the correct task, confirmation and cancellation, out-of-range selections, deleting the last task, renumbering after deletion, and persistence of the removal. Explain the distinction between displayed numbers and list indexes.
> - Editing: discuss permitted fields, retaining unchanged values, positive estimated minutes, blank input, invalid selections, preserving completion status unless I explicitly allow changing it, and saving the revised task.
> - File-based help: discuss a menu option, the help file's content and location beside the application, reading it when requested, missing or unreadable files, and returning to the menu afterward.
> - Additional analytics: define just my selected measure, distinguish total planned time from remaining time if relevant, address empty lists and zero denominators where applicable, and preserve existing summary meanings.
>
> After giving the plan, stop and let me implement it. In follow-up questions, continue explaining and reviewing without supplying code or pseudocode. If I later request code, remind me of this activity's AI-Assisted boundary and offer a conceptual explanation instead.

## After Receiving the Plan

Record your decisions before implementing. Work through the checkpoints and collect actual results, including failures and revisions. Update your AI-use justification with what the AI contributed and what you decided, wrote, and verified yourself. Choose the next backlog feature only after you can demonstrate and explain the current extension.
