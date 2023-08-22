import os
from app.treeview import Treeview
from app.renny import RennyTheLittleGuy
from app.background import Background
from app.console import Console
from app.chatbox import Chatbox
from app.settings import SETTINGS
import tkinter as tk
import time
import json

# Dear sir, I would like to complain about that last tutorial about people not writing unit tests.
# I myself have coded all my life without testing 
# and... have... never... once... AAHHHH! [ImportError: attempted relative import with no known parent package]


class Renny:

    def __init__(self,root):

        self.desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.root = root

        self.running=True
        self.openWindows = []
        self.menues = []
        self.t = 1

        self.state = self.load_state()
        self.path = self.state["Path"]


        #                Label                        Func                             Checkable?           Checked?           Default?   
        self.items = [("Open communicator",    lambda: self.open_gui(Chatbox),           False,              None,             True),
                      ("Find",                 self.find,                                False,              None,             False),
                      ("See activity",         lambda: self.open_gui(Console),           False,              None,             False),
                      ("SEPARATOR",            None,                                     False,              None,             False),
                      ("Settings",             self.open_settings,                       False,              None,             False),
                      ("Running",              self.toggle_running,                      True,               self.running,     False),
                      ("Exit",                 self.on_exit,                             False,              None,             False)]
        
        

    def load_state(self):
        try:
            #file_path = os.path.join(desktop, "config.cfg")  # Use the same file_path used in save_config()
            
            with open("state.cfg", "r") as state_file:
                return json.loads(state_file.read())

        except FileNotFoundError:
            return {"Path":""}
            #return {}
        
    def save_state(self):
        with open("state.cfg", "w") as state_file:
                json.dump(self.state,state_file)


    def run(self):
        if self.path == "":
            self.firstTime()
        else:
            print(self.path)
            #self.main(self.path)
            

    def firstTime(self):
        treeview = Treeview(self.root,self.releaseRenny)
        self.setup = SETTINGS(treeview)
        self.setup.load_settings()
        self.releaseButton = tk.Button(treeview, text="Release Renny", command=treeview.submit_info)
        self.releaseButton.pack()
        root.mainloop()


    def open_settings(self):
        root = tk.Toplevel(self.root)
        self.settings = SETTINGS(root)
        
    def releaseRenny(self, path):
        self.setup.save_settings()
        #self.settings = self.setup.settings

        try:
            with open("log.txt", "r") as log_file:
                self.log = json.loads(log_file.read())
        except FileNotFoundError:
            pass


        self.path = path
        self.root.withdraw()
        print(f"Renny is released at {path}")

        self.renny = RennyTheLittleGuy(path)


        self.background = Background(path)

        self.background.setup_daemon_thread(self.scheduledActivity)
        self.background.setup_system_tray(self.items)

    def scheduledActivity(self):
        while True:
            if self.running:
                print(f"Current windows: {self.openWindows}")
                time.sleep(self.t)


    def interactWithRenny(self):
        self.background.setup_daemon_thread(self.sendMessage)

    def sendMessage(self):
        print("Loading response...")
        response = self.renny.listFolders(self.path)
        self.saveLog(response)
        self.running = False
        #self.renny.perform(response,0)
        self.running = True

    def saveLog(self,response):
        self.log = []
        
        try:
            with open("log.txt", "r") as log_file:
                self.log = json.loads(log_file.read())
        except FileNotFoundError:
            pass
        with open("log.txt","w") as log_file:
            self.log.append(json.loads(response))
            json.dump(self.log,log_file,indent=4)


    def toggle_running(self):
        self.running = not self.running
        self.update_menu()

    def update_menu(self):
        for menu in self.menues:
            for boolean in menu.booleans:
                boolean[1].set(self.running)
        for i in range(len(self.background.checkables)):
            self.background.checkables[i] = self.running


    def on_exit(self, icon, item):
        print("Closing application")
        self.root.destroy()
        icon.stop()


    def open_gui(self,obj):


        if (obj.__name__) not in self.openWindows:

            self.background.icon.stop()
            root = tk.Toplevel(self.root)

            frame = obj(root)

            menu = MenuCreator(root)
            menu.construct_menu(self.items)
            tk.Button(frame,text="Force interaction",command=self.interactWithRenny).pack()
            
            print(f"{obj.__name__} opened")
            self.openWindows.append(obj.__name__)
            self.menues.append(menu)
            root.protocol('WM_DELETE_WINDOW', lambda: self.withdraw_window(root,obj,menu))

            try:
                frame.initialize(self.log)
            except AttributeError:
                print("what the heck")
            self.update_menu()

        else:
            print("Window already opened")


    def withdraw_window(self,root,obj,menu):
        
        root.destroy()
        self.openWindows.remove(obj.__name__)
        self.menues.remove(menu)
        if not self.openWindows:
            for child in self.root.winfo_children():
                if isinstance(child, tk.Toplevel):
                    child.destroy()
            self.background.setup_system_tray(self.items)
        


    def find(self):
        print("Opening folder")




    '''def killChatbox(self):
        self.chatbox.destroy()
        self.chatbox_root.withdraw()
        self.windows.remove(self.chatbox)
        if not self.windows:
            self.background.setup_system_tray(self.items)

    def killConsole(self):
        self.console.destroy()
        self.console_root.withdraw()
        self.windows.remove(self.console)
        if not self.windows:
            self.background.setup_system_tray(self.items)'''
    
class MenuCreator(tk.Menu):

    def __init__(self,root):
        super().__init__(root)

        root.config(menu=self)

        self.booleans = []
        

    def construct_menu(self, items):

        self.options_menu = tk.Menu(self, tearoff=0)
        
        self.add_cascade(label="Options", menu=self.options_menu)

        for label, func, checkable, checked, default in items:
            self.options_menu.add
            if label == "SEPARATOR":
                self.options_menu.add_separator()
            elif checkable:
                value = tk.BooleanVar()
                value.set(checked)
                self.booleans.append((label,value))
                self.options_menu.add_checkbutton(label="Running", variable=self.booleans[-1][1], command=func)
            else:
                self.options_menu.add_command(label=label, command=func)

        self.options_menu.add_command(label="Set token", command=lambda:print("Set token"))
        self.options_menu.add_command(label="Set character", command=lambda:print("Set character"))
        self.options_menu.add_command(label="Open website...", command=lambda:print("Open website..."))
        


'''    def save_config(self):
        config_data = {
            "path": "",
            "other": ""
        }

        #file_path = os.path.join(desktop, "config.cfg")
        with open("config.cfg", "w") as config_file:
            config_file.write(path)
            #json.dump(config_data, config_file)



        return path

    def killRenny(self):
        try:
            os.remove('runn.ing')
            print("File deleted successfully.")
        except OSError as e:
            print(f"Error: {e}")

    def main(self, path):

        
        with open('runn.ing', 'w') as file:
            file.write('Renny is running.')


        # Start the main loop
        #root = tk.Tk()
        app = chatbox.cb(root)
        root.mainloop()


        print("File created successfully.")'''
        
        




if __name__ == "__main__":
    root = tk.Tk()
    renny = Renny(root)
    renny.run()