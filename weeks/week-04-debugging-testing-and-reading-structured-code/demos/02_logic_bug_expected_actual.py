"""
Week 4 Demo 2: logic bug and expected vs actual output

Purpose:
Show that code can run but still produce the wrong answer.

Instructor note:
Run the program first, then ask what result was expected.
"""


def calculate_discount(price, discount_rate):
    discount = price * discount_rate
    final_price = price + discount  # Bug: should subtract the discount.
    return final_price


original_price = 100
rate = 0.20

expected = 80
actual = calculate_discount(original_price, rate)

print("Expected:", expected)
print("Actual:", actual)

