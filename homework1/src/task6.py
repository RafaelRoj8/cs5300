# src/task6.py
# A generic counter that takes a file path,
# plus a helper that finds task6_read_me.txt no matter where tests run.


# imports os for safe path handling and existence checks
import os


def count_words_in_file(path):
    # Reads the file at 'path' and returns how many words it contains.
    # A "word" here is any chunk separated by whitespace so spaces/newlines/tabs.
   

    # checks that the file actually exists
    if not os.path.exists(path):
        # raises a clear error if the path is wrong or the file is missing
        raise FileNotFoundError(f"File not found: {path}")

    # opens the file in text mode with UTF-8 encoding
    with open(path, "r", encoding="utf-8") as f:
        # reads the entire file into a single string
        text = f.read()

    # splits the string on whitespace to get a list of words
    words = text.split()

    # counts how many items are in that list
    count = len(words)

    # returns the number to the caller
    return count


def count_words_in_task6_readme():
    # Locates 'task6_read_me.txt' in the homework1 folder and count its words.
    
    # gets the folder of THIS file which is in /homework1/src
    here = os.path.dirname(__file__)
    # goes up one level to the homework1 folder
    homework1 = os.path.dirname(here)
    # builds the full path to task6_read_me.txt
    txt_path = os.path.join(homework1, "task6_read_me.txt")

    # uses the function so the logic stays in one place
    return count_words_in_file(txt_path)


# runs only when this file is executed directly won't run during tests/imports
if __name__ == "__main__":
    # prints the count for task6_read_me.txt
    print("Words in task6_read_me.txt:", count_words_in_task6_readme())

