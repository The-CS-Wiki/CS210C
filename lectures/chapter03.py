import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017")
db = client["AcmeCorporation"]
col = db["users"]

res = col.find({"age": 20})
for i in res:
    print(i)

col.delete_many({"age": 20})

print()
res = col.find({"age": 20})
for i in res:
    print(i)
