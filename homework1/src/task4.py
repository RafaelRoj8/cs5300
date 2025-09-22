# src/task4.py

def calculate_discount(price, discount):
    """
    Per the instructions this program returns the final price after applying a percent discount.

    - price: numeric int or float
    - discount: numeric percent like 20 means 20%

    I use variables a and b inside.
    """

    # a holds the original price
    a = price            
    # b holds the discount percent
    b = discount         

    # Turn the percent into a fraction
    discount_fraction = b / 100

    # Compute how much money is taken off
    discount_amount = a * discount_fraction

    # Subtract the discount from the original price
    final_price = a - discount_amount

    # Give the answer back to the caller
    return final_price


if __name__ == "__main__":
    # quick manual checks (not used in tests)
    print(calculate_discount(100, 20))     # 80.0
    print(calculate_discount(59.99, 15.5)) # ~50.79155
