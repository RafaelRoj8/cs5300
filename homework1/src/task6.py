# src/task6.py

def count_words_in_task6_readme():
    # Opens the text file that lives in the *same* homework1 folder where we run tests.

    # "r" = read-only; UTF-8 handles normal text well.
    with open("task6_read_me.txt", "r", encoding="utf-8") as f:
        # Reads the entire file into one big string.
        text = f.read()

    # Splits the string on whitespace so spaces/newlines/tabs to get a list of words.
    words = text.split()

    # The word count is just how many items are in that list.
    count = len(words)

    # Gives the number back to the caller.
    return count


if __name__ == "__main__":
    # Manually checks but this is not used by tests
    print(count_words_in_task6_readme())
