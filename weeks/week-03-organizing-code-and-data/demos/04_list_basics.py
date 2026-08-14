"""
Week 3 Demo 4: list basics

Purpose:
Show that a list stores multiple related values.

Instructor note:
Use this to reinforce index, append, and iteration without going too deep.
"""

tasks = ["read chapter", "write notes", "practice Python"]

print("First task:", tasks[0])
print("All tasks:")

for task in tasks:
    print("-", task)

tasks.append("submit assignment")

print("Updated tasks:")
for task in tasks:
    print("-", task)

