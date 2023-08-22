from app.api import chat
from app.utils.folder import list_files_and_folders,go_back,extension
from app.utils.file import read_pdf_text,read_docx_text,read_txt
from app.console import Console
import tkinter as tk
import json


class RennyTheLittleGuy:
    def __init__(self, path):

        self.path = path

        self.text_types = [".txt",".pdf",".docx"]



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

        response = chat(msg)

        # Parsing the JSON string
        data = json.loads(response)
        keys = list(data.keys())


        # Accessing the data
        self.mind = data['mind']
        self.action = keys[1]
        self.file = data[self.action]

        print(self.mind)

        #self.perform(self.action,self.file,self.index)
        
    def perform(self,action,file,i):
        if action == "stand-by":
            print("He wants to stand-by at "+self.path)
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
        if action == "keep-reading":
            print("He wants to keep reading "+file)
        if action == "open-folder":
            print("He wants to open "+file)
        if action == "write-journal":
            print("He wants to write on his journal")

if __name__ == "__main__":
    Renny = RennyTheLittleGuy("G:/Benja 2010")
    #Renny.setup_system_tray(10)
