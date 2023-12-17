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
            "product_id": "P1001",
            "name": "UltraWidget 2000",
            "category": "Electronics",
            "price": 199.99,
            "ratings": [
                {"rating": 4.5, "reviewer": "John Doe"},
                {"rating": 4.0, "reviewer": "Jane Smith"},
            ],
            "stock": 50,
            "details": {"manufacturer": "Widget Corp", "brand": "Ultra"},
            "tags": ["gadget", "tech", "latest"],
        },
        {
            "product_id": "P1002",
            "name": "MegaGadget Pro",
            "category": "Gadgets",
            "price": 149.99,
            "ratings": [
                {"rating": 5.0, "reviewer": "Alice Johnson"},
                {"rating": 4.5, "reviewer": "Bob Brown"},
            ],
            "stock": 30,
            "details": {"manufacturer": "GadgetWorks", "brand": "Mega"},
            "tags": ["gadget", "tech", "new"],
        },
        {
            "product_id": "P1003",
            "name": "SuperTool Kit",
            "category": "Tools",
            "price": 89.99,
            "ratings": [{"rating": 4.0, "reviewer": "Charlie Davis"}],
            "stock": 75,
            "details": {"manufacturer": "ToolMakers", "brand": "Super"},
            "tags": ["tool", "diy", "home", "discount"],
        },
    ]
)

# TODO: Connect to the local MongoDB server
client =

# TODO: Select a database called "practice_db" and
# TODO:     collection called "practice_collection"
db =
col =






# PROBLEM 1
# TODO: Using the selected collections and databases, insert ONE document that
# TODO:     has the following information:
# TODO:         product_id = P1004
# TODO:         name = Olive Oil
# TODO:         category = Food
# TODO:         price = 45.99
# TODO:         ratings = []    # Empty List
# TODO:         stock = 300
# TODO:         details = {"manufacturer": "Olive Garden", "brand": "Olives"}
# TODO:         tags = ["cooking", "home"]


# Check user's input
try:
    res = col.find_one({"product_id": {"$eq": "P1004"}})
    if not res["details"] == {
        "manufacturer": "Olive Garden",
        "brand": "Olives",
    }:
        print("Problem 1 is incorrect")
        exit()
except Exception:
    print("Problem 2 is incorrect")
    exit()





# PROBLEM 2
# TODO: Using the selected collections and databases, find ALL document that
# TODO:     have a stock of less than or equal to 50
res = 

# Check user's input
try:
    for i in res:
        if i["product_id"] not in ["P1001", "P1002"]:
            print("Problem 2 is incorrect")
            exit()
except Exception:
    print("Problem 2 is incorrect")
    exit()





# PROBLEM 3
# TODO: Using the selected collections and databases, find ONE document that
# TODO:     has the "discount"
# TIP:  The query, {"field": {"$in": [a, b, ..]}}, finds documents that have
# TIP:      any one of the following elements [a, b, ...]
res = 

# Check user's input
try:
    if not res["product_id"] == "P1003":
        print("Problem 3 is incorrect")
        exit()
except Exception as e:
    print("Problem 3 is incorrect")
    print(e)
    exit()






# Print the medal!
print("Practice 2 Complete! \n")
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
