#
#  Author: Benjamin Herrera
#
#  CS210C // Basics of MongoDB
#  Chapter 1: Terminologies and Pymongo
#  Practice 1, Pymongo
#

""" You are tasked to complete the TODO's of this practice file. Fill out the
code necessary to attain the correct information
"""

# Imports
from pymongo import MongoClient
from utils import setup, drop

# Run setup
""" These are the documents that have been inserted for pratice. Use this 
as reference for completing this practice
"""
setup(
    [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25},
        {"name": "Charlie", "age": 35},
    ]
)

# TODO: Connect to the local MongoDB server

# TODO: Select a database called "practice_db" and 
# TODO:     collection called "practice_collection"

# PROBLEM 1
# TODO: Using the selected collections and databases, get ONE document that 
# TODO:     has a key "age" with a value of 25
res = 

# Check user's input
if not res["name"] == "Bob":
    print("Problem 1 is incorrect")
    exit() 


# PROBLEM 2
# TODO: Using the selected collections and databases, get ONE document that 
# TODO:     has a key "name" with a value of "Charlie"
res = 

# Check user's input
if not res["age"] == 35:
    print("Problem 2 is incorrect")
    exit() 
    
# Print the medal!
print("Practice 1 Complete! \n")
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
