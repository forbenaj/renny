from app.api import chat
from app.utils.folder import list_files_and_folders,go_back,extension
from app.utils.file import read_pdf_text,read_docx_text,read_txt
from app.console import Console
import tkinter as tk
import json
import os
import time


class RennyTheLittleGuy:
    def __init__(self, path):

        self.path = path # Do we need this path here?

        self.text_types = [".txt",".pdf",".docx"]


    def sendData(self,state):

        path = state["Path"]
        action = state["Action"]
        file = state["File"]
        index = state["Index"]
        sent_msg = state["Sent_msg"]

        message = ""

        if sent_msg:
            message = "User: "+sent_msg

        elif action == "begin": # The "begin" action is only given on the first run
            message = self.listFolders(path)

        elif action == "open-folder":
            print("He wants to open "+file)
            path = path+"/"+file
            message = self.listFolders(path+"/"+file)

        elif action == "close-folder":
            print("He wants to open go back, close "+file)
            message = self.listFolders(go_back(path))

        elif action == "open-file" or action =="keep-reading":
            if extension(file) == ".txt":
                content,index, eof = read_txt(path+"/"+file,index)
                act = "are" if action == "open-file" else "continue"
                end = "> Keep reading or close file?" if not eof else "end of file."
                message = f'You {act} reading "{file}"\n"{content}"\n{end}'
            else:
                message = "This is not a text file\n"+self.listFolders(path)
                index="0"
        
        elif action == "write-journal":
            print("He wants to write on his journal")

        #response = chat(message)
        print("Pretending to get data...")
        time.sleep(5)
        response = '{"mind": "Hellot here!!","open-folder": "Mis Cosas"}'
        data = json.loads(response)

        data["path"] = path
        data["index"] = index
        data["talking"] = False


        return data

    def listFolders(self,path):

        self.path = path
        status,files,folders = list_files_and_folders(path)

        msg = ""

        if status == "ok":

            msg = f'You are at "{self.path}"\n'

            msg += "Files:\n"

            for file in files[:20]:
                msg += file + "\n"

            msg += "Folders:\n"

            for folder in folders[:20]:
                msg += folder + "\n"
            
            msg += "> What will you do?"
        elif status == "not-found":
            msg = f'Folder not found: "{self.path}"\n'
        elif status == "denied":
            msg = f'Permission denied: "{self.path}"\n'

        return msg

        
    def getData(self,response,i):
        # Parsing the JSON string
        data = json.loads(response)
        keys = list(data.keys())

        # Accessing the data
        mind = data['mind']
        action = keys[1]
        file = data[action]


        print(mind)
        if action == "open-file":
            print("He wants to check "+file)
            if action == "open-file":
                newIndex=0
            if extension(file) == ".txt":
                result,newIndex = read_txt(self.path+"/"+file,i)
            else:
                result = "This is not a text file"
                newIndex="0"
            return result,newIndex
        if action == "open-folder":
            print("He wants to open "+file)
        if action == "keep-reading":
            print("He wants to keep reading "+file)
        if action == "write-journal":
            print("He wants to write on his journal")
            

if __name__ == "__main__":
    Renny = RennyTheLittleGuy("G:/Benja 2010")
    i = 0
    while True:
        action = input("Specify next action:\n")
        state = {
            "Path":"C:/Users/Admin/Desktop",
            "Action":action,
            "File":"test.txt",
            "Index":i}
        response, i = Renny.sendData(state)
    #Renny.setup_system_tray(10)
