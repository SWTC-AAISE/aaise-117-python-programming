"""
Week 1 Demo 2: strings and variable updates

Purpose:
Show that variables can be reassigned and used to build output.

Instructor note:
Use this to reinforce that a variable name points to a current value.
"""

favorite_language = "Python"
status = "new"

print("Favorite language:", favorite_language)
print("Current status:", status)

status = "learning"

print("Updated status:", status)

sentence = "I am " + status + " " + favorite_language + "."
print(sentence)

