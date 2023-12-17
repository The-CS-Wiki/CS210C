import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["AcmeCorporation"]
col = db["users"]
res = col.find_one({"age": 20})

print(res)
