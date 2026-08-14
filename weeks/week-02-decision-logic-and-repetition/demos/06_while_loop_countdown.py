"""
Week 2 Demo 6: while loop with a stopping condition

Purpose:
Show that a while loop continues while a condition is True.

Instructor note:
Point out the update line. Without it, this loop would never stop.
"""

countdown = 5

while countdown > 0:
    print("Countdown:", countdown)
    countdown = countdown - 1

print("Liftoff!")

