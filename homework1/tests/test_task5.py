# tests/test_task5.py

# Import the functions we want to test from task5.
from src.task5 import make_books_list, first_three_books, make_student_db


def test_books_list_and_slice():
    # builds the full book list from the function
    books = make_books_list()                     

    # the outer container will be a LIST
    assert isinstance(books, list)               

    # checks each item in the list
    for item in books:

        # each item should be a dictionary                            
        assert isinstance(item, dict) 

        # every book in the dict needs a 'title' key
        assert "title" in item   

        # every book in the dict also needs an 'author' key                 
        assert "author" in item                   

    # what I expect the first three books to be and the order matters
    expected_first_three = [
        {"title": "The Secret", "author": "Rhonda Byrne"},                # 1st
        {"title": "Think and Grow Rich", "author": "Napoleon Hill"},      # 2nd
        {"title": "The Psychology of Money", "author": "Morgan Housel"},  # 3rd
    ]

    # here it uses the slicing helper to get the first three and compare
    # slice result from the list
    actual_first_three = first_three_books(books)  
    # lists of dicts should match exactly
    assert actual_first_three == expected_first_three  

    # here it also checks the 4th item specifically so index 3
    fourth = books[3]                               # get the 4th book
    assert fourth["title"] == "Seedtime and Harvest (1956)"  # correct title
    assert fourth["author"] == "Neville Goddard"             # correct author


def test_student_db_structure_and_lookup():
    # build the dictionary from the function
    db = make_student_db()                

    # it should be a dictionary
    assert isinstance(db, dict)           

    # iterate over key/value pairs
    for name, student_id in db.items():   

        # keys should be student names in strings
        assert isinstance(name, str) 

        # values should be IDs as integers
        assert isinstance(student_id, int)  

    # spot-check a couple of known entries
    assert db["Alice"] == 1001

    # .get also works for lookups
    assert db.get("Carlos") == 1003       
