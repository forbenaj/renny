from api import chat
from folder import list_files,go_back
import json

def currently(action,target):
    if action == "stand-by":
        print("Remmy is standing at "+path)
    if action == "reading-file":
        print("Remmy is checking "+target)
    if action == "writing-journal":
        print("Remmy is writing on his journal")

def perform(action,target):
    if action == "stand-by":
        print("He wants to stand-by at "+path)
    if action == "read-file":
        print("He wants to check "+target)
    if action == "open-folder":
        print("He wants to open "+target)
    if action == "write-journal":
        print("He wants to write on his journal")

path="G:/Benaj/Pictures"

files = list_files(path)

firstTenFiles = files[:10]

msg = f'"{path}"\n'

#for file in files:
for file in firstTenFiles:
    msg = msg + file + "\n"

response = chat(msg)

#print(msg)
#print(response)

# Parsing the JSON string
data = json.loads(response)

# Accessing the data
current_action = data['current-action']
current_target = data['current-target']
mind = data['mind']
next_action = data['next-action']
next_target = data['next-target']
print(mind)

currently(current_action,current_target)

perform(next_action,next_target)