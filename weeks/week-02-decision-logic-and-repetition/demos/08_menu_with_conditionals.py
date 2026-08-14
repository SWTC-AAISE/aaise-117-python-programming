"""
Week 2 Demo 8: menu with loops and conditionals

Purpose:
Show conditionals and loops working together in a small menu.

Instructor note:
This is a bridge demo toward mini-programs. Keep it small and avoid adding
functions here unless students are ready.
"""

choice = ""

while choice != "3":
    print()
    print("Menu")
    print("1. Say hello")
    print("2. Show course")
    print("3. Quit")

    choice = input("Choose an option: ")

    if choice == "1":
        print("Hello!")
    elif choice == "2":
        print("Course: Python Programming")
    elif choice == "3":
        print("Goodbye!")
    else:
        print("That option is not available.")

