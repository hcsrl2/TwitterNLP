import pymongo

# Connect to the MongoDB server and select the database
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["database_name"]

# Get a list of all the collections in the database
collections = db.list_collection_names()

# Use a for loop to iterate over the collections
for collection_name in collections:
    # Select the collection
    collection = db[collection_name]

    # Use another for loop to iterate over the documents in the collection
    for document in collection.find():
        # Access the data in each document
        print(document)

# Close the connection to the MongoDB server
client.close()
