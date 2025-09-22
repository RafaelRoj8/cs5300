# src/task5.py

# In this task we are asked to me lists and dictionaries.
# I keep the titles names simple and use variables a and b where it makes sense.


def make_books_list():
    """Return a LIST of favorite books. Each book is a DICTIONARY."""

    a = {"title": "The Secret", "author": "Rhonda Byrne"}            # first book
    b = {"title": "Think and Grow Rich", "author": "Napoleon Hill"}  # second book
    c = {"title": "The Psychology of Money", "author": "Morgan Housel"}  # third book
    d = {"title": "Seedtime and Harvest (1956)", "author": "Neville Goddard"}  # fourth

    # put the 4 book dictionaries into one LIST and the order matters
    books = [a, b, c, d]     

    # give the list back to whoever called the function
    return books             


def first_three_books(books):
    # Using LIST SLICING, return only the first 3 items from a book list.

    # slice from index 0 up to but not including index 3
    first_three = books[:3]
    # returns the slice  
    return first_three       


def make_student_db():
    # Return a DICTIONARY that maps student names into str to IDs into int.

     # store the whole database in variable a
    a = {                   
        "Alice": 1001,       # key = name (string), value = student ID (integer)
        "Bob": 1002,
        "Carlos": 1003,
        "Diana": 1004,
    }
    # returns the dictionary
    return a                 


if __name__ == "__main__":  
    # build the list 
    my_books = make_books_list()  
    # demo of slicing                     
    print("First three:", first_three_books(my_books)) 

    # build the student DB
    db = make_student_db() 
    # dictionary looks up example                           
    print("Alice's ID:", db["Alice"])                  
