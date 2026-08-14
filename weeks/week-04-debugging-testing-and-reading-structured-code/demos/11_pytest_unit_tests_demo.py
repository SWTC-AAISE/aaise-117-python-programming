"""
Week 4 Demo 11: pytest unit tests

Purpose:
Show a small but realistic pytest example.

Instructor note:
This is a recognition-level introduction to pytest. Students do not need to
master testing architecture here. The goal is to see that professional tests
are usually written as repeatable checks, not as ad hoc print statements.

Run this demo with:
python -m pytest 11_pytest_unit_tests_demo.py
"""

from unittest.mock import Mock

import pytest


def calculate_order_total(subtotal, discount_rate, tax_rate):
    discount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount
    tax = discounted_subtotal * tax_rate
    return discounted_subtotal + tax


def letter_grade(score):
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    if score >= 60:
        return "D"
    return "F"


def get_tax_rate(zip_code, rate_lookup):
    """Use a lookup dependency so the function can be tested without a network call."""
    return rate_lookup(zip_code)


def test_calculate_order_total_applies_discount_before_tax():
    result = calculate_order_total(100, 0.10, 0.055)

    assert result == pytest.approx(94.95)


@pytest.mark.parametrize(
    "score, expected",
    [
        (100, "A"),
        (90, "A"),
        (89, "B"),
        (80, "B"),
        (79, "C"),
        (70, "C"),
        (69, "D"),
        (60, "D"),
        (59, "F"),
    ],
)
def test_letter_grade_boundaries(score, expected):
    assert letter_grade(score) == expected


def test_get_tax_rate_uses_lookup_dependency():
    fake_lookup = Mock(return_value=0.055)

    result = get_tax_rate("53081", fake_lookup)

    assert result == 0.055
    fake_lookup.assert_called_once_with("53081")


def test_get_tax_rate_can_use_a_different_lookup_result():
    fake_lookup = Mock(return_value=0.06)

    result = get_tax_rate("90210", fake_lookup)

    assert result == 0.06
    fake_lookup.assert_called_once_with("90210")


if __name__ == "__main__":
    print("Run this file with pytest:")
    print("python -m pytest 11_pytest_unit_tests_demo.py")

