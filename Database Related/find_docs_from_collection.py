from pymongo import MongoClient

# Connect to the MongoDB server
client = MongoClient("mongodb://localhost:27017/")

# Choose the database
db = client["mydb"]

# Get a list of all collections in the database
collections = db.list_collection_names()

# Iterate over the collections
for collection_name in collections:
    collection = db[collection_name]
    print("Collection name:", collection_name)

    # Iterate over the documents in the collection
    for document in collection.find():
        print("Document:", document)





