# tests/test_task6.py

# Import the very simple word-count function.
from src.task6 import count_words_in_task6_readme


def test_word_count_matches_manual_read():
    # Ask our function for the count.
    found = count_words_in_task6_readme()

    # Compute the "manual" expected count by opening the same file
    # and doing the same .split() approach right here.
    with open("task6_read_me.txt", "r", encoding="utf-8") as f:
        manual = len(f.read().split())

    # They should match exactly.
    assert found == manual


def test_returns_int():
    # The result should be an integer (number of words).
    assert isinstance(count_words_in_task6_readme(), int)
