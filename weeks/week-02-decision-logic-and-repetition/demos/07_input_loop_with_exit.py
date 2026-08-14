"""
Week 2 Demo 7: input loop with exit condition

Purpose:
Show repeated input and a clear stopping condition.

Instructor note:
This is interactive. Use it only after students have seen input() and while loops.
"""

command = ""

while command != "quit":
    command = input("Enter a command, or type 'quit' to stop: ")
    print("You entered:", command)

print("Program ended.")

