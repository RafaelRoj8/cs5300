# tests/test_task2.py

# imports the functions we will test
from src.task2 import use_int, use_float, use_str, use_bool


def test_int_type_and_value():
    # calls the function to get the integer
    v = use_int()
    # verifies the type is int
    assert isinstance(v, int)
    # verifies the value is 42
    assert v == 42


def test_float_type_and_value():
    # calls the function to get the float
    v = use_float()
    # verifies the type is float
    assert isinstance(v, float)
    # verifies the value is 5.0
    assert v == 5.0


def test_str_type_and_value():
    # calls the function to get the string
    v = use_str()
    # verifies the type is str
    assert isinstance(v, str)
    # verifies the exact text
    assert v == "Hello, World!"


def test_bool_type_and_value():
    # calls the function to get the boolean
    v = use_bool()
    # verifies the type is bool
    assert isinstance(v, bool)
    # verifies the value is True
    assert v is True
