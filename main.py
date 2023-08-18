import os
import app.treeview as treeview
from app.renny import RennyTheLittleGuy
from app.background import Background
from app.behaviour import Console
from app.chatbox import Chatbox
import tkinter as tk
import time

# Dear sir, I would like to complain about that last tutorial about people not writing unit tests.
# I myself have coded all my life without testing 
# and... have... never... once... AAHHHH! [ImportError: attempted relative import with no known parent package]


class Renny:

    def __init__(self,root):

        self.desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        self.root = root
        #self.root.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.running=True
        self.path = self.load_config()
        self.windows = []

        #                Label                  Func                Checkable?           Checked?           Default?   
        self.items = [("Open communicator",    self.communicator,      False,              None,             True),
                      ("Find",                 self.find,              False,              None,             False),
                      ("See activity",         self.see_activity,      False,              None,             False),
                      ("SEPARATOR",            None,                   False,              None,             False),
                      ("Running",              self.toggle_running,    True,               self.running,     False),
                      ("Exit",                 self.on_exit,           False,              None,             False)]
        

    def load_config(self):
        try:
            #file_path = os.path.join(desktop, "config.cfg")  # Use the same file_path used in save_config()
            
            with open("config.cfg", "r") as config_file:
                return config_file.read()

        except FileNotFoundError:
            return ""


    def run(self):
        if self.path == "":
            self.firstTime()
        else:
            print(self.path)
            #self.main(self.path)

    def firstTime(self):
        self.selectPath = treeview.tv(self.root,self.releaseRenny)
        root.mainloop()
        
    def releaseRenny(self, path):
        self.selectPath.destroy()
        self.root.withdraw()
        print(f"Renny is released at {path}")

        #Renny = RennyTheLittleGuy(path)

        #console = Console

        self.background = Background(path)

        self.background.setup_daemon_thread(1,self.scheduledActivity)
        self.background.setup_system_tray(self.items)



    def scheduledActivity(self,t):
        i=""
        while True:
            if self.running:
                print(f"Current windows: {self.windows}")
            time.sleep(t)

    def toggle_running(self):
        self.running = not self.running

    def on_exit(self, icon, item):
        print("Closing application")
        self.root.destroy()
        icon.stop()

    def communicator(self):
        
        self.background.icon.stop()
        
        root = self.root if self.windows == [] else tk.Toplevel(self.root)

        self.construct_menu(root)

        print("Communicator opened")
        self.chatbox = Chatbox(root)
        button = tk.Button(self.chatbox,text="kill",command=self.chatbox.destroy)
        button.pack()
        self.windows.append(self.chatbox)
        print(f"This is {self.chatbox}")
        root.protocol('WM_DELETE_WINDOW', lambda: self.withdraw_window(self.chatbox,root))
        self.root.after(0, self.root.deiconify)

    def find(self):
        print("Opening folder")

    def see_activity(self):
        self.background.icon.stop()

        root = self.root if self.windows == [] else tk.Toplevel(self.root)
            
        self.construct_menu(root)

        print("Behaviour opened")
        self.console = Console(root)
        self.windows.append(self.console)
        root.protocol('WM_DELETE_WINDOW', lambda: self.withdraw_window(self.console,root))
        self.root.after(0, self.root.deiconify)

    def withdraw_window(self,window,root):
        window.destroy()
        root.withdraw()
        self.windows.remove(window)
        if not self.windows:
            self.background.setup_system_tray(self.items)

    
    def construct_menu(self,root):
        
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)
        
        for label, func, checkable, checked, default in self.items:
            self.options_menu.add
            if label == "SEPARATOR":
                self.options_menu.add_separator()
            elif checkable:
                self.boolean = tk.BooleanVar()
                self.boolean.set(self.running)
                self.options_menu.add_checkbutton(label="Running", variable=self.boolean, command=func)
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