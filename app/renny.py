from api import chat
from utils.folder import list_files_and_folders,go_back,extension
from utils.file import read_pdf_text,read_docx_text,read_txt
import json


def perform(action,file,i):
    if action == "stand-by":
        print("He wants to stand-by at "+path)
    if action == "open-file":
        print("He wants to check "+file)
        if action == "open-file":
            newIndex=0
        if extension(file) == ".txt":
            result,newIndex = read_txt(path+"/"+file,i)
        else:
            result = "This is not a text file"
            newIndex="0"
        return result,newIndex
    if action == "keep-reading":
        print("He wants to keep reading "+file)
    if action == "open-folder":
        print("He wants to open "+file)
    if action == "write-journal":
        print("He wants to write on his journal")


index = 0

text_types = [".txt",".pdf",".docx"]

path="G:/Benja 2010"

status,files,folders = list_files_and_folders(path)

msg = ""

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

perform(action,file,index)