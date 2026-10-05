# Suggested AI Prompt: VS Code Workspace Version

Use this version in VS Code's embedded AI chat with the Course Task Tracker project available in the workspace. The [original prompt](suggested_ai_prompt.md) includes more background for conversations where files must be supplied separately.

Choose one backlog feature: task deadlines, deletion, editing, file-based help, or one additional summary measure from the working-plan backlog. Fill in the three placeholders below, then submit the prompt in chat. Implement and validate that feature before choosing another.

## Student Prompt

> Help me plan one backlog feature for the Course Task Tracker in AI-Assisted mode. I will make the decisions, write the code, test it, and explain the result.
>
> - Selected feature: [choose one].
> - User need and desired behavior: [describe why it matters and what the user should be able to do].
> - My decisions or open questions: [state relevant choices, or say undecided].
>
> **Inspect the workspace first.** Locate the project's Capstone_Example folder and read README.md, working_plan.md, main.py, validation_checks.py, tasks.json, and ai_use_justification.md. Base your advice on the current files, including any features already added. If there are multiple copies of the project, ask which one to use. If you cannot access a needed file, identify it before giving advice that depends on its contents.
>
> **Stay in planning mode.** Give plain-language explanations and steps only. Do not generate code, pseudocode, patches, implementation snippets, or executable commands. Do not edit files or run the application. Plan only the selected feature, using the existing beginner-level structure and standard library. Ask focused questions where a decision materially changes the plan; leave final choices to me. Keep this boundary in follow-up replies.
>
> Provide a detailed but focused plan with:
>
> 1. **Success criteria:** describe observable behavior for the selected feature and identify unresolved decisions.
> 2. **Affected responsibilities:** name the relevant files and functions, explain how their responsibilities would change, and address data fields, existing saved tasks, persistence, and menu behavior where applicable. Preserve the existing relationship between the application and validation script.
> 3. **Implementation steps:** order the work into small steps. For each step, explain what I should change, why, and what observable checkpoint I should use after implementing it. Explain unfamiliar concepts without translating the steps into code or pseudocode.
> 4. **Test scenarios:** provide a table of starting conditions or inputs, expected results, and manual versus function-level checks. Cover normal use, invalid input, empty or boundary cases, and save/reload behavior where relevant. Include regression checks for existing features and explain how to interpret the current validation script's results. Do not claim proposed tests have passed.
> 5. **Documentation and ownership:** identify documentation I should revise and questions to answer in my AI-use justification about suggestions accepted, changed, or rejected, my decisions, and actual test evidence. Finish with a short completion checklist and questions that check whether I can explain my implementation.
>
> Address the important edge cases for my selected feature: existing tasks without deadline fields and valid dates; deletion confirmation and renumbering; retaining values during editing; locating and reading the help file; or defining the selected summary measure and handling empty data. Include only the cases relevant to my choice. Stop after the plan so I can implement it myself.

## Student Follow-Through

Review the plan and resolve its open decisions. Write and test your implementation, record actual outcomes, and update your AI-use justification. Be ready to explain the feature before moving to the next backlog item.
