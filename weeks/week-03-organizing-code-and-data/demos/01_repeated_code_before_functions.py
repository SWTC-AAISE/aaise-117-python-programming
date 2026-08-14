"""
Week 3 Demo 1: repeated code before functions

Purpose:
Show why repeated code becomes hard to maintain.

Instructor note:
This is intentionally not ideal. Use it as the "before" example before
introducing function-based structure.
"""

price_1 = 12.00
tax_rate = 0.055
total_1 = price_1 + (price_1 * tax_rate)
print("Item 1 total:", total_1)

price_2 = 25.00
tax_rate = 0.055
total_2 = price_2 + (price_2 * tax_rate)
print("Item 2 total:", total_2)

price_3 = 7.50
tax_rate = 0.055
total_3 = price_3 + (price_3 * tax_rate)
print("Item 3 total:", total_3)

