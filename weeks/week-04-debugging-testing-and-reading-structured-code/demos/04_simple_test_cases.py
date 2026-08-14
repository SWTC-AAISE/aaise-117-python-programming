"""
Week 4 Demo 4: simple test cases

Purpose:
Show that a function can be checked with several expected results.

Instructor note:
This is not a full testing framework yet. Keep it simple and readable.
"""


def is_passing(score):
    return score >= 70


print("Test 1:", is_passing(90), "Expected:", True)
print("Test 2:", is_passing(70), "Expected:", True)
print("Test 3:", is_passing(69), "Expected:", False)

