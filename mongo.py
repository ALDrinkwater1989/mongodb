import pymongo
import os

MONGODB_URI = os.getenv("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION_NAME = "myFirstMDB"

def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailur as e:
        print("could not connect to MongoDB: %s") % e
conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION_NAME]

coll.update_one({'first': 'george'}, {'$set' : {'nationality': 'american'}})

documents = coll.find({'nationality': 'american'})
for doc in documents:
    print(doc)
