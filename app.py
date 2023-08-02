from api import chat
from folder import list_files_and_folders,go_back
import json

def perform(action,file):
    if action == "stand-by":
        print("He wants to stand-by at "+path)
    if action == "read-file":
        print("He wants to check "+file)
    if action == "open-folder":
        print("He wants to open "+file)
    if action == "write-journal":
        print("He wants to write on his journal")

path="C:/Users/Admin/Desktop/renny"

status,files,folders = list_files_and_folders(path)

if status == "ok":

    msg = f'You are at "{path}"\n'

    msg += "Files:\n"

    for file in files[:20]:
        msg += file + "\n"

    msg += "Folders:\n"

    for folder in folders[:20]:
        msg += folder + "\n"
    
    msg += "> What will you do?"
elif status == "not-found":
    msg = f'Folder not found: "{path}"\n'
elif status == "denied":
    msg = f'Permission denied: "{path}"\n'

response = chat(msg)

# Parsing the JSON string
data = json.loads(response)
keys = list(data.keys())


# Accessing the data
mind = data['mind']
action = keys[1]
file = data[action]

print(mind)

perform(action,file)