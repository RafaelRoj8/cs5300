# src/task2.py
# The task requiremnts ask to use integers, floats, strings, and booleans.


def use_int() -> int:
    # Returns an integer result using two integer variables a and b.

    # creates the first integer
    a = 21
    # creates the second integer
    b = 21
    # adds the two integers
    result = a + b
    # returns the sum
    return result


def use_float() -> float:
    # Return a float result using two float variables a and b.

    # creates the first float
    a = 10.0
    # creates the second float
    b = 4.0
    # divides a by b to get a float
    part = a / b
    # multiplies the result by 2
    result = part * 2
    # returns the final float
    return result


def use_str() -> str:
    # Returns a string made by concatenating a and b.

    # creates the first piece of text
    a = "Hello, "
    # creates the second piece of text
    b = "World!"
    # joins the two strings
    result = a + b
    # returns the combined string
    return result


def use_bool() -> bool:
    # Returns a boolean using simple logic with a and b.

    # sets a to True
    a = True
    # sets b to False
    b = False
    # computes True AND but NOT False
    result = a and (not b)
    # returns the boolean result
    return result


# runs main only when this file is executed directly
if __name__ == "__main__":

    # prints the integer result
    print(use_int())
    # prints the float result
    print(use_float())
    # prints the string result
    print(use_str())
    # prints the boolean result
    print(use_bool())
