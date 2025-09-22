# tests/test_task4.py

# The program imports the function that needs to be tested from the task4 module.
from src.task4 import calculate_discount

# pytest is the testing library we are using for approx on floats.
import pytest


def test_int_price_int_discount():
    # In this test, both a and b are integers.
    # a = price, b = discount percent
    a = 100      # price is $100
    b = 20       # discount is 20%

    # Call the function we are testing.
    result = calculate_discount(a, b)

    # 20% of 100 is 20, so final price should be 80.
    # result may be 80.0 in float data type. 80 == 80.0 is True in Python so it should pass.
    assert result == 80


def test_float_price_float_discount():
    # Here, a and b are floats.
    a = 59.99    # price is $59.99
    b = 15.5     # discount is 15.5%

    # What we expect mathematically:
    # final = price * (1 - discount/100)
    expected = a * (1 - b / 100)

    # Call the function to get the actual result.
    result = calculate_discount(a, b)

    # Because floats can have tiny rounding differences,
    # we compare using pytest.approx (checks "close enough").
    assert result == pytest.approx(expected, rel=1e-9)


def test_int_price_float_discount():
    # Mixed types also work (duck typing): int price, float discount.
    a = 200      # $200
    b = 12.5     # 12.5% off

    expected = a * (1 - b / 100)
    result = calculate_discount(a, b)

    # Use approx again because we used a float discount.
    assert result == pytest.approx(expected, rel=1e-9)


def test_float_price_int_discount():
    # Another mixed case: float price, int discount.
    a = 80.0     # $80.00
    b = 25       # 25% off

    expected = a * (1 - b / 100)
    result = calculate_discount(a, b)

    assert result == pytest.approx(expected, rel=1e-9)
