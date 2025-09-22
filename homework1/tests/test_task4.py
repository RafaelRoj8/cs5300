# tests/test_task4.py

# imports pytest for approx() and raises()
import pytest
# imports the function I am testing
from src.task4 import calculate_discount


def test_int_price_int_discount():
    # chooses an integer price
    a = 100
    # chooses an integer discount percent
    b = 20
    # calls the function to get the result
    result = calculate_discount(a, b)
    # verifies the final price is 80
    assert result == 80


def test_float_price_float_discount():
    # chooses a float price
    a = 59.99
    # chooses a float discount percent
    b = 15.5
    # computes the expected value by hand
    expected = a * (1 - b / 100)
    # calls the function to get the result
    result = calculate_discount(a, b)
    # compares floats using approx
    assert result == pytest.approx(expected, rel=1e-9)


def test_int_price_float_discount():
    # chooses an int price
    a = 200
    # chooses a float discount percent
    b = 12.5
    # computes the expected value
    expected = a * (1 - b / 100)
    # calls the function
    result = calculate_discount(a, b)
    # compares with approx
    assert result == pytest.approx(expected, rel=1e-9)


def test_float_price_int_discount():
    # chooses a float price
    a = 80.0
    # chooses an int discount percent
    b = 25
    # computes the expected value
    expected = a * (1 - b / 100)
    # calls the function
    result = calculate_discount(a, b)
    # compares with approx
    assert result == pytest.approx(expected, rel=1e-9)


def test_validation_non_numeric_price():
    # expects a TypeError when price is not a number
    with pytest.raises(TypeError):
        calculate_discount("100", 10)


def test_validation_non_numeric_discount():
    # expects a TypeError when discount is not a number
    with pytest.raises(TypeError):
        calculate_discount(100, "10")


def test_validation_negative_price():
    # expects a ValueError for negative price
    with pytest.raises(ValueError):
        calculate_discount(-1, 10)


def test_validation_discount_below_zero():
    # expects a ValueError for discount < 0
    with pytest.raises(ValueError):
        calculate_discount(100, -5)


def test_validation_discount_above_100():
    # expects a ValueError for discount > 100
    with pytest.raises(ValueError):
        calculate_discount(100, 120)
