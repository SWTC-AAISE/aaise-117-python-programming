"""
Week 4 Demo 3: fixed logic bug

Purpose:
Show the corrected version of the discount calculation.

Instructor note:
Compare this with 02_logic_bug_expected_actual.py.
"""


def calculate_discount(price, discount_rate):
    discount = price * discount_rate
    final_price = price - discount
    return final_price


original_price = 100
rate = 0.20

expected = 80
actual = calculate_discount(original_price, rate)

print("Expected:", expected)
print("Actual:", actual)
print("Correct:", expected == actual)

