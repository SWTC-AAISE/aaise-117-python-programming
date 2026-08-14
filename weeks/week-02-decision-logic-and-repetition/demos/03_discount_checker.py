"""
Week 2 Demo 3: decision logic in a practical example

Purpose:
Show a small decision-based program that changes output based on conditions.

Instructor note:
This can bridge toward Assignment 2 without being the same as a student solution.
"""

purchase_total = 42.00
discount_threshold = 50.00
discount_rate = 0.10

print("Purchase total:", purchase_total)

if purchase_total >= discount_threshold:
    discount = purchase_total * discount_rate
    final_total = purchase_total - discount
    print("Discount applied:", discount)
    print("Final total:", final_total)
else:
    print("No discount applied.")
    print("Final total:", purchase_total)

