
#import pymongo

#client=pymongo.MongoClient("mongodb://localhost:27017/")
#db=client['messages']
#collections = db['conservation']


# db.py
from pymongo import MongoClient
from pymongo.collection import Collection

client = MongoClient("mongodb://localhost:27017/")
db = client["chat_history"]
collection = db["conversations"]

def get_collection() -> Collection:
    return collection


#documents= [
    #{"name": "Faranstain","age":"78"},
    #{"name": "opra","age":"78"}]

#collections.insert_many(documents)
#print("inserted")
#client.close()


