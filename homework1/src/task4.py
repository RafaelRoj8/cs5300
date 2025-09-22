# src/task4.py


def calculate_discount(price, discount):
   
    # Returns the final price after applying a percent discount.
    # - price: number in int or float, must be >= 0
    # - discount: number also in int or float as a percent, must be in [0, 100]
    

    # checks that price is a number in  int or float
    if not isinstance(price, (int, float)):
        # raises an error if price is not numeric
        raise TypeError("price and discount must be numbers")

    # checks that discount is a number 
    if not isinstance(discount, (int, float)):
        # raises an error if discount is not numeric
        raise TypeError("price and discount must be numbers")

    # checks that price is not negative
    if price < 0:
        # raises an error if price is negative
        raise ValueError("price must be non-negative")

    # checks that discount is between 0 and 100 
    if not (0 <= discount <= 100):
        # raises an error if discount is out of range
        raise ValueError("discount must be between 0 and 100")

    # stores the original price in a 
    a = price
    # stores the discount percent in b
    b = discount
    # converts percent to a fraction 
    discount_fraction = b / 100
    # computes the amount taken off
    discount_amount = a * discount_fraction
    # subtracts the discount from the original price
    final_price = a - discount_amount
    # returns the final price
    return final_price


# run only when this file is executed directly
if __name__ == "__main__":
    # prints an example1 like: 20% off of 100 -> 80.0
    print(calculate_discount(100, 20))
    # prints an example2 like: 15.5% off of 59.99
    print(calculate_discount(59.99, 15.5))

