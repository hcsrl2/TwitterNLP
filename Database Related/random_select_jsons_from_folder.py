import os
import random

# Define the path to the folder containing the JSON files
folder_path = 'path/to/folder'

# Get a list of all the JSON files in the folder
json_files = [f for f in os.listdir(folder_path) if f.endswith('.json')]

# Calculate the number of files to select (10% of the total number of files)
num_files_to_select = int(0.1 * len(json_files))

# Select the files randomly
selected_files = random.sample(json_files, num_files_to_select)

# Print the selected files
print(selected_files)