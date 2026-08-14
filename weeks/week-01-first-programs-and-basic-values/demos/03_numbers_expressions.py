"""
Week 1 Demo 3: numbers and expressions

Purpose:
Show numeric values, basic arithmetic, and storing calculated results.

Instructor note:
Connect each printed result back to the value flow:
starting values -> expression -> stored result -> output.
"""

items_purchased = 3
price_each = 4.50

subtotal = items_purchased * price_each
tax_rate = 0.055
tax_amount = subtotal * tax_rate
total = subtotal + tax_amount

print("Items purchased:", items_purchased)
print("Price each:", price_each)
print("Subtotal:", subtotal)
print("Tax:", tax_amount)
print("Total:", total)

