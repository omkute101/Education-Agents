import json
import os

MEMORY_FILE = os.path.join(os.path.dirname(__file__), "memory.json")

# Initialize memory if file doesn't exist
if not os.path.exists(MEMORY_FILE):
    with open(MEMORY_FILE, "w") as f:
        json.dump({}, f, indent=4)

def get_memory(user_id: str, key: str):
    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)
    if user_id not in data:
        data[user_id] = {}
    return data[user_id].get(key, "NOT_SET")

def set_memory(user_id: str, key: str, value):
    with open(MEMORY_FILE, "r") as f:
        data = json.load(f)
    if user_id not in data:
        data[user_id] = {}
    data[user_id][key] = value
    with open(MEMORY_FILE, "w") as f:
        json.dump(data, f, indent=4)
