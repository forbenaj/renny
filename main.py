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
        self.root.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.running=True
        self.path = self.load_config()
        self.currentWindow = ""

        self.items = [("Open communicator", self.communicator, False, True),
                      ("Find", self.find, False, False),
                      ("See activity", self.see_activity, False, False),
                      ("SEPARATOR",None, False, False),
                      ("Running", self.toggle_running,True, False),
                      ("Exit", self.on_exit, False, False)]
        

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
        self.root.mainloop()
        
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
            if self.background.running:
                i=i+"."
                print("Doing smthn"+i)
                i= "" if len(i) > 2 else i
            time.sleep(t)

    def toggle_running(self, icon, item):
        self.background.running = not self.background.running

    def on_exit(self, icon, item):
        print("Closing application")
        self.root.destroy()
        icon.stop()

    def communicator(self):
        self.construct_menu()
        self.background.icon.stop()
        print("Communicator opened")
        self.currentWindow = "Communicator"
        self.chatbox = Chatbox(self.root)
        self.root.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        self.root.after(0, self.root.deiconify)

    def find(self):
        print("Opening folder")

    def see_activity(self):
        #self.construct_menu()
        self.background.icon.stop()
        print("Behaviour opened")
        self.currentWindow = "Behaviour"
        self.console_root = tk.Toplevel(self.root)
        self.console = Console(self.console_root)
        #self.root.protocol('WM_DELETE_WINDOW', self.withdraw_window)
        #self.root.after(0, self.root.deiconify)

    def withdraw_window(self):
        self.root.withdraw()
        self.background.setup_system_tray(self.items)

    def construct_menu(self):
        #self.root = tk.Tk()
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)
        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)
        self.options_menu.add_command(label="Find", command=self.find)
        self.options_menu.add_command(label="See activity", command=self.see_activity)
        self.options_menu.add_checkbutton(label="Running", variable=tk.BooleanVar(), command=self.toggle_running)
        self.options_menu.add_separator()
        self.options_menu.add_command(label="Set token", command=print("Set token"))
        self.options_menu.add_command(label="Set character", command=print("Set character"))
        self.options_menu.add_command(label="Open website...", command=print("Open website..."))
        self.options_menu.add_command(label="Exit", command=self.on_exit)



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