"""
Week 2 Demo 5: accumulator pattern

Purpose:
Show how a loop can update a running total.

Instructor note:
Trace the value of total after each loop cycle. This is a core mental model
for later data and list processing.
"""

total = 0

for number in range(1, 6):
    total = total + number
    print("Added:", number, "Current total:", total)

print("Final total:", total)

