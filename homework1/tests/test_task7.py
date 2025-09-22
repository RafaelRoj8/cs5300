# tests/test_task7.py

# Import the two functions we wrote in task7.
from src.task7 import elementwise_add, average_of_list
# for approx when checking floats
import pytest

def test_elementwise_add_basic():
    # Use a and b lists with simple integers
    a = [1, 2, 3]
    b = [4, 5, 6]

    # Call the function and check the exact list we expect
    result = elementwise_add(a, b)
    assert result == [5, 7, 9]

def test_average_of_list_basic():
    # A small list of even numbers
    nums = [2, 4, 6, 8]

    # The average should be 5.0
    result = average_of_list(nums)
    assert result == pytest.approx(5.0)
