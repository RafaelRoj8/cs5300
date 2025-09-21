# tests/test_task3.py

# Import the three functions we want to test from the task3 module.
from src.task3 import classify_number, first_primes, sum_1_to_100


def test_classify_number():
    # Positive number should return the string "positive"
    assert classify_number(12) == "positive"

    # Negative number should return the string "negative"
    assert classify_number(-5) == "negative"

    # Zero should return the string "zero"
    assert classify_number(0) == "zero"


def test_first_10_primes():
    # The first 10 prime numbers are well-known.
    # We check that our function returns exactly this list.
    expected = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]  # expected results
    actual = first_primes(10)                        # calls the function
    assert actual == expected                        # verifies they match exactly


def test_sum_1_to_100():
    # The sum 1+2+...+100 equals 5050.
    # We check that the while-loop implementation returns that value.
    assert sum_1_to_100() == 5050

