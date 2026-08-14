"""
Week 4 Demo 5: assert basics

Purpose:
Show a lightweight way to check expected behavior.

Instructor note:
Use this only if students are ready. Otherwise, stay with print-based checks.
"""


def add_tax(price, tax_rate):
    return price + (price * tax_rate)


assert add_tax(100, 0.05) == 105
assert add_tax(0, 0.05) == 0
assert add_tax(50, 0.10) == 55

print("All checks passed.")

