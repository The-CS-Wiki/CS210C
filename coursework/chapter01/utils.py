#
#  Author: Benjamin Herrera
#

# Imports
from pymongo import MongoClient

# Connect to the local MongoDB server
CLIENT = MongoClient("localhost", 27017)


def setup(data):
    """Sets up the practice file"""
    # Focus on the DB and collection
    db = CLIENT["practice_db"]
    col = db["practice_collection"]

    # Seed the database with given data
    col.insert_many(data)


def drop():
    CLIENT.drop_database("practice_db")
    CLIENT.close()
