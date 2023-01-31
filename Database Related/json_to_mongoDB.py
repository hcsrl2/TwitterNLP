import os
import json
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['your_database_name']

# Specify the folder containing the JSON files
folder = 'path/to/json/files'

# Iterate through the files in the folder
for filename in os.listdir(folder):
    if filename.endswith('.json'):
        file_path = os.path.join(folder, filename)
        # Open the file and load the JSON data
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)
        # Insert the data into MongoDB
        db.your_collection_name.insert_one(data)

# Print a message to confirm that the files have been inserted
print('JSON files have been inserted into MongoDB')