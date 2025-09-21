# src/task2.py

def use_int() -> int:
    """Use integers a and b and return a simple result."""
    a = 21
    b = 21
    return a + b  # 42


def use_float() -> float:
    """Use floats a and b and return a simple result."""
    a = 10.0
    b = 4.0
    return (a / b) * 2  # 5.0


def use_str() -> str:
    """Use strings a and b and return their concatenation."""
    a = "Hello, "
    b = "World!"
    return a + b


def use_bool() -> bool:
    """Use booleans a and b and return a logical result."""
    a = True
    b = False
    return a and (not b)  # True


if __name__ == "__main__":
    print(use_int(), use_float(), use_str(), use_bool())
