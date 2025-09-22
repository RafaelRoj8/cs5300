# tests/test_task2.py
# This file shows a *parameterized* test: one test function
# runs multiple times with different inputs/expected results.

# imports pytest so we can use @pytest.mark.parametrize
import pytest
# import the functions we want to test
from src.task2 import use_int, use_float, use_str, use_bool

# tell pytest to run the test below once for each tuple we provide
@pytest.mark.parametrize(
    # this is the parameter name the test function will receive
    "fn, expected, type_",
    # this is the list of (function, expected_value, expected_type) tuples
    [
        # case 1: integer function should return 42 (int)
        (use_int, 42, int),
        # case 2: float function should return 5.0 (float)
        (use_float, 5.0, float),
        # case 3: string function should return "Hello, World!" (str)
        (use_str, "Hello, World!", str),
        # case 4: boolean function should return True (bool)
        (use_bool, True, bool),
    ],
)
def test_types_and_values(fn, expected, type_):
    # calls the function to get the actual value
    v = fn()
    # check that the type matches what we expect
    assert isinstance(v, type_)
    # check that the value matches what we expect
    assert v == expected
