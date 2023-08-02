from api import chat
from folder import list_files,go_back
import json

def perform(action,target):
    if action == "stand-by":
        print("He wants to stand-by at "+path)
    if action == "read-file":
        print("He wants to check "+target)
    if action == "open-folder":
        print("He wants to open "+target)
    if action == "write-journal":
        print("He wants to write on his journal")

path="G:/Benja 2010/Imágenes Benja"

files = list_files(path)

msg = f'"{path}"\n'

#for file in files:
for file in files[:20]:
    msg = msg + file + "\n"

response = chat(msg)

# Parsing the JSON string
data = json.loads(response)

# Accessing the data
currently = data['currently']
mind = data['mind']
next_action = data['next-action']
target = data['target']

print(currently)
print(mind)


perform(next_action,target)