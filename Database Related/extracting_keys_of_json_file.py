import json

# Load JSON data from a file
with open("data.json") as f:
    data = json.load(f)


def list_keys(example, parent=None):
    """
    Recursive function to list all keys of a dictionary, preserving the hierarchy
    """
    keys = []
    for key, value in example.items():
        if parent:
            full_key = f"{parent}.{key}"
        else:
            full_key = key
        if isinstance(value, dict):
            keys.extend(list_keys(value, full_key))
        else:
            keys.append(full_key)
    return keys


# Get all keys of the dictionary
keys = list_keys(data)

# Write keys to a new JSON file
with open("keys.json", "w") as f:
    json.dump(keys, f)
