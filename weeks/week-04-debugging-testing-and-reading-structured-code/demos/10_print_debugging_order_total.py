"""
Week 4 Demo 10: print debugging an order total

Purpose:
Show how a program can produce a plausible but wrong total when one step in
the calculation uses the wrong value.

Instructor note:
This is a good demo for "signal in the noise." The final number is wrong, but
the real clue is found by printing subtotal, discount, tax, and total at each
stage.
"""


cart_items = [
    {"name": "notebook", "price": 4.50, "quantity": 3},
    {"name": "pen pack", "price": 6.00, "quantity": 2},
    {"name": "folder", "price": 2.25, "quantity": 4},
]


def calculate_total_buggy(items, discount_rate, tax_rate):
    subtotal = 0

    for item in items:
        line_total = item["price"] * item["quantity"]
        subtotal += line_total

        # Print-debugging checkpoint 1:
        # print(item["name"], "line total:", line_total)
        # print("Subtotal so far:", subtotal)

    discount = subtotal * discount_rate

    # Bug: tax should be calculated after the discount is applied.
    tax = subtotal * tax_rate
    total = subtotal - discount + tax

    # Print-debugging checkpoint 2:
    # print("Subtotal:", subtotal)
    # print("Discount:", discount)
    # print("Tax:", tax)
    # print("Final total:", total)

    return total


def calculate_total_with_debug_output(items, discount_rate, tax_rate):
    subtotal = 0

    for item in items:
        line_total = item["price"] * item["quantity"]
        subtotal += line_total

        print(item["name"], "line total:", line_total)
        print("Subtotal so far:", subtotal)

    discount = subtotal * discount_rate
    tax = subtotal * tax_rate
    total = subtotal - discount + tax

    print("Subtotal:", subtotal)
    print("Discount:", discount)
    print("Tax:", tax)
    print("Final total:", total)

    return total


def calculate_total_fixed(items, discount_rate, tax_rate):
    subtotal = 0

    for item in items:
        line_total = item["price"] * item["quantity"]
        subtotal += line_total

    discount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * tax_rate
    total = discounted_subtotal + tax

    return total


discount = 0.10
tax = 0.055

print("BROKEN VERSION")
print("Actual total:", calculate_total_buggy(cart_items, discount, tax))
print("Expected total:", 32.75775)

print("\nPROGRESSIVE PRINT-DEBUGGING VERSION")
calculate_total_with_debug_output(cart_items, discount, tax)

print("\nFIXED VERSION")
print("Fixed total:", calculate_total_fixed(cart_items, discount, tax))
