#
#  Author: Benjamin Herrera
#
#  CS210C // Basics of MongoDB
#  Chapter 3: Update and Delete
#  Practice 4, Update and Delete
#

""" You are tasked to complete the TODO's of this practice file. Fill out the
code necessary to attain the correct information
"""

# Imports
import traceback
from pymongo import MongoClient
from utils import setup, drop

# Run setup
""" These are the documents that have been inserted for pratice. Use this 
as reference for completing this practice
"""
setup(
    [
        {
            "book_id": "B1001",
            "title": "The Great Gatsby",
            "author": "F. Scott Fitzgerald",
            "year_published": 1925,
            "genres": ["Novel", "Fiction"],
            "copies_available": 5
        },
        {
            "book_id": "B1002",
            "title": "1984",
            "author": "George Orwell",
            "year_published": 1949,
            "genres": ["Dystopian", "Political fiction"],
            "copies_available": 3
        },
        {
            "book_id": "B1003",
            "title": "To Kill a Mockingbird",
            "author": "Harper Lee",
            "year_published": 1960,
            "genres": ["Southern Gothic", "Legal Story"],
            "copies_available": 4
        }
    ]
)

# TODO: Connect to the local MongoDB server
client = MongoClient("mongodb://localhost:27017")

# TODO: Select a database called "practice_db" and
# TODO:     collection called "practice_collection"
db = client["practice_db"]
col = db["practice_collection"]





# PROBLEM 1
# TODO: Update the title of the book with book_id B1002 to "Nineteen Eighty-Four"


# Check user's input
try:
    res = col.find_one({"book_id": "B1002"})
    if not res["title"] == "Nineteen Eighty-Four":
        print("Problem 1 is incorrect")
        exit()
except Exception as e:
    print("Problem 3 is incorrect")
    print(e)
    exit()





# PROBLEM 2
# TODO: Set the copies_available of all books published before 1950 to 2


# Check user's input
try:
    count = 0
    res = col.find({"year_published": {"$lt": 1950}})
    for doc in res:
        if doc["copies_available"] != 2:
            print("Problem 2 is incorrect")
            exit()
        count += 1
    if count != 2:
        print("Problem 2 is incorrect")
        exit()
except Exception as e:
    print("Problem 3 is incorrect")
    print(e)
    exit()





# PROBLEM 3
# TODO: Delete the book with the title "To Kill a Mockingbird"


# Check user's input
try:
    res = col.find_one({"title": "To Kill a Mockingbird"})
    if res is not None:
        print("Problem 3 is incorrect")
        exit()
except Exception as e:
    print("Problem 3 is incorrect")
    print(e)
    exit()





# Completion Message
print("Practice 3 Complete! \n")
print(
    """
         _______________
        |@@@@|     |####|
        |@@@@|     |####|
        |@@@@|     |####|
        \\@@@@|     |####/
         \\@@@|     |###/
          `@@|_____|##'
               (O)
            .-'''''-.
          .'  * * *  `.
         :  *       *  :
        : ~ Practice  ~ :
        : ~ Completed ~ :
         :  *       *  :
          `.  * * *  .'
            `-.....-'
              \n"""
)

# Drop the practice database
drop()