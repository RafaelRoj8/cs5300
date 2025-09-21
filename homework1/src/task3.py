# src/task3.py

def classify_number(n):
    # Decides if the input number n is positive, negative, or zero.
    # The code returns a small string that names the case.

    # if n is greater than zero
    if n > 0:         

        # It will return "positive"
        return "positive"  

     # otherwise, if n is less than zero
    elif n < 0:   

        # it will return "negative"
        return "negative" 

    # if neither of the above was true, n must be zero        
    else:      

       # or returns "zero"               
        return "zero"         


def is_prime(n):
    # Determine if n is a prime number using very simple checks.
    # A prime is an integer >= 2 that has no divisors except 1 and itself.

    # numbers 0 and 1 and negatives are NOT prime
    if n < 2:                 
        return False

    # Try dividing n by every number from 2 up to n-1.
    # If any divides evenly, n is NOT prime.

    # d takes values 2, 3, 4, ..., n-1
    for d in range(2, n):     

        # "%" is remainder; remainder 0 means "divides evenly"
        if n % d == 0:        

            # found a divisor -> composite, not prime
            return False      

    # loop finished with no divisors -> n is prime
    return True               


def first_primes(count=10):
    # Build and return a list with the first `count` prime numbers.
    # We use a for-loop over a range that's big enough to find the first 10.

    # starts with an empty list to collect primes
    primes = []               

    # 200 is comfortably large to contain the first 10 primes.
    # num will be 2, 3, 4, ..., 199
    for num in range(2, 200): 

        # check if current number is prime
        if is_prime(num):     

            # if yes, add it to the list
            primes.append(num)  

        # stops early once we have the requested amount
        if len(primes) == count:  

            # break will exit the for-loop immediately
            break                  

    # give back the completed list (length == count)
    return primes              

 
# Uses a while-loop to add the numbers from 1 through 100 (inclusive).
def sum_1_to_100():
    
    # runs sum and starts at 0
    total = 0  

    # loop counter starts at 1              
    i = 1                     

    # while loop keeps looping while i is 1..100
    while i <= 100:   

        # adds the current i into the running total        
        total = total + i  

        # moves i forward by 1 or the loop never ends   
        i = i + 1             

    # final sum; should be 5050
    return total              

# This block only runs if you execute this file directly.
if __name__ == "__main__":
    
    # example output: "positive"
    print(classify_number(5))     
    # example output: first 10 primes list
    print(first_primes(10))   
     # example output: 5050    
    print(sum_1_to_100())        