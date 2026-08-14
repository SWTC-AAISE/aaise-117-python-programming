"""
Week 1 Demo 5: input and number conversion

Purpose:
Show that input() returns text, and numeric input must be converted before math.

Instructor note:
This is a common early stumbling block. Demonstrate the error first only if
students are ready; otherwise show the correct pattern directly.
"""

first_number_text = input("Enter the first number: ")
second_number_text = input("Enter the second number: ")

first_number = float(first_number_text)
second_number = float(second_number_text)

total = first_number + second_number

print("First number:", first_number)
print("Second number:", second_number)
print("Total:", total)

