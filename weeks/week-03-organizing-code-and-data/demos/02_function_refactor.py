"""
Week 3 Demo 2: refactoring repeated code into a function

Purpose:
Show how a function names repeated logic and makes code easier to reuse.

Instructor note:
Compare this directly to 01_repeated_code_before_functions.py.
"""


def calculate_total(price, tax_rate):
    tax_amount = price * tax_rate
    total = price + tax_amount
    return total


tax_rate = 0.055

item_1_total = calculate_total(12.00, tax_rate)
item_2_total = calculate_total(25.00, tax_rate)
item_3_total = calculate_total(7.50, tax_rate)

print("Item 1 total:", item_1_total)
print("Item 2 total:", item_2_total)
print("Item 3 total:", item_3_total)

