"""
Week 2 Demo 2: if / elif / else grade check

Purpose:
Show how a program chooses between multiple branches.

Instructor note:
Change the score live and rerun the program. Ask students which branch should
run before executing.
"""

score = 84

print("Score:", score)

if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
elif score >= 60:
    print("Grade: D")
else:
    print("Grade: F")

