# tests/test_task6.py
# From the rubric I need to tests for robust file I/O.
# And use parametrize for multiple cases and also test missing-file errors.

# imports pytest for parametrize and raises
import pytest
# imports os only to build a manual path for the readme comparison
import os
# imports the functions we are testing
from src.task6 import count_words_in_file, count_words_in_task6_readme


@pytest.mark.parametrize(
    "text, expected",
    [
        # empties file -> 0 words
        ("", 0),
        # single word
        ("one", 1),
        # three words separated by single spaces
        ("one two three", 3),
        # multiple spaces and a newline still count as whitespace
        (" spaced   out \n lines ", 3),
    ],
)
def test_count_words_in_file_param(tmp_path, text, expected):
    # creates a temporary file path
    p = tmp_path / "sample.txt"
    # writes the chosen text into the file
    p.write_text(text, encoding="utf-8")
    # calls the function and compare with the expected count
    assert count_words_in_file(p) == expected


def test_count_words_in_task6_readme_matches_manual():
    # calls the function that locates and counts the readme file
    found = count_words_in_task6_readme()

    # builds the file path manually to compute the expected value here
    here = os.path.dirname(__file__)
    homework1 = os.path.dirname(here)
    txt_path = os.path.join(homework1, "task6_read_me.txt")

    # opens and splits the same file to get the manual count
    with open(txt_path, "r", encoding="utf-8") as f:
        manual = len(f.read().split())

    # the function's result and the manual count should match exactly
    assert found == manual


def test_missing_file_raises(tmp_path):
    # chooses a path that does not exist
    missing = tmp_path / "does_not_exist.txt"
    # expects FileNotFoundError when we try to count it
    with pytest.raises(FileNotFoundError):
        count_words_in_file(missing)

