import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["AcmeCorporation"]
col = db["users"]

# ! INSERTION
# col.insert_one({"name": "Kara", "age": 62, "email": "kara@mail.com"})
# col.insert_many(
#     [
#         {"name": "Kara", "age": 62, "email": "kara@mail.com"},
#         {"name": "Kara", "age": 62, "email": "kara@mail.com"},
#     ]
# )

# ! FIND
res = col.find({"email": {"$exists": True}})
for i in res:
    print(i)
