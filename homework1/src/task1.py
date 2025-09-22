# src/task1.py

# This task defines a tiny function that prints a message "Hello World".

def hello():
   
    # Prints 'Hello, World!' to the screen.
    # The built-in print() function writes text to "standard output" (stdout),
    # which is what you normally see in the terminal.
    print("Hello, World!")  # print the exact message


# This is the main guard
# When the file is *imported* (e.g., by tests), __name__ is NOT "__main__",
# The code below will NOT run during tests.
if __name__ == "__main__":
    # Calls the function so we see the message when running this file by itself.
    hello()

