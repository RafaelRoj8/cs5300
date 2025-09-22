# src/task7.py

# We will use the NumPy package to do simple math.
import numpy as np  # "np" is the common short name

#Add two lists of numbers, position by position, using NumPy.
# like this for example: a=[1,2,3], b=[4,5,6] -> [5,7,9]
def elementwise_add(a, b):
    
    
    
    # turn list a into a NumPy array
    a_array = np.array(a)   
     # turn list b into a NumPy array
    b_array = np.array(b)     

    # NumPy adds arrays element-by-element
    sum_array = a_array + b_array   

    # convert back to a normal Python list
    return sum_array.tolist()  


# Return the average (mean) of a list of numbers using NumPy.
def average_of_list(numbers):
  
    # make a float array from the list
    arr = np.array(numbers, dtype=float)
    # NumPy computes the mean for us  
    mean_value = np.mean(arr) 
    # make sure we return a plain float           
    return float(mean_value)              

# This isnt used by the test
if __name__ == "__main__":
    
    a = [1, 2, 3]
    b = [4, 5, 6]
    print("elementwise_add:", elementwise_add(a, b))
    print("average_of_list:", average_of_list([2, 4, 6, 8]))
