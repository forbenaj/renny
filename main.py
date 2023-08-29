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

        self.desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop') # UNUSED. Prolly will need it for the Renny House
        self.root = root

        self.running=True
        self.openWindows = [] # Store the currently open windows (currently only Chatbox and Console. Setup is not considered a window)
        self.menues = [] # Stores the "Options" menu in every window, to be able to update the booleans
        self.t = 1 # Sleep time for scheduled function, in seconds

        self.state = self.load_state() # Current state of Renny.

        # Get the values from the state. May not need it in the main script
        self.path = self.state["Path"]
        self.action = self.state["Action"]
        self.file = self.state["File"]
        self.index = self.state["Index"]

        # This dictionary contains the items for the tray and the options menu

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
            #file_path = os.path.join(desktop, "config.cfg")  # Use the same file_path used in save_config() # UNUSED
            
            with open("state.cfg", "r") as state_file:
                return json.loads(state_file.read())

        except FileNotFoundError:
            return {"Path":"","Action":"","File":""}
            #return {}
        
    def save_state(self):
        with open("state.cfg", "w") as state_file:
                json.dump(self.state,state_file)



    # Program begins here. Will consider first time if path is empty
    def run(self):
        if self.path == "":
            self.firstTime()
        else:
            print(self.path)
            #self.main(self.path)
            

    def firstTime(self):
        treeview = Treeview(self.root,self.releaseRenny) # Creates the path selection window. Includes releaseRenny as a callback
        self.setup = SETTINGS(treeview)
        self.setup.load_settings()
        self.releaseButton = tk.Button(treeview, text="Release Renny", command=treeview.submit_info) # When button is presse, selected path is passed to the callback
        self.releaseButton.pack()
        root.mainloop() # This sets the tkinter loop. Main thread is now at use.

    # MOVE THIS, PROLLY WITH OTHER WINDOWS
    def open_settings(self):
        root = tk.Toplevel(self.root)
        self.settings = SETTINGS(root)
        


    # Program REALLY starts here
    def releaseRenny(self, path):
        self.setup.save_settings()
        #self.settings = self.setup.settings

        # Get the log for the console later. May be sketchy, consider other options. Also it repeats.
        try:
            with open("log.txt", "r") as log_file:
                self.log = json.loads(log_file.read())
        except FileNotFoundError:
            pass


        self.path = path
        self.root.withdraw() # This withdraws the main tkinter window, taking it out of the main thread
        print(f"Renny is released at {path}")


        # Renny himself. Handles communication with Renny back and forth
        self.renny = RennyTheLittleGuy(path)

        # Handles all background tasks, like tray and daemon threads
        self.background = Background(path)

        self.background.setup_daemon_thread(self.scheduledActivity) # Daemon thread for the automatic Renny behaviour

        self.background.setup_system_tray(self.items)
        #It is NECCESARY to withdraw any tkinter window to be able to run the tray, as it also uses the main thread




    # This should make for the automatic behaviour of the little guy. Currently used as real time window logger
    def scheduledActivity(self):
        while True:
            if self.running:
                print(f"Current windows: {self.openWindows}")
                time.sleep(self.t)




    # Setup the function to communicate with Renny via the api. This needs a daemon thread because it takes a shit ton of seconds and holds the thread forever
    def interactWithRenny(self):
        self.background.setup_daemon_thread(self.sendMessage)


    def sendMessage(self):
        print("Loading response...")
        
        # This fella holds the thread until we get a response from the server

        response = self.renny.listFolders(self.path) # THIS ONE SHOULD BE ANOTHER FUNCTION, LIKE "SENDMESSAGE"

        self.saveLog(response) # Add current message to the log, so the Console can read it

        data = json.loads(response)
        keys = list(data.keys())

        # Accessing the data
        mind = data['mind']
        action = keys[1]
        file = data[action]

        self.running = False # Not sure if this should be here? I think I set it to False to ensure no message is sent again before the thread is done, so it should be up
        #self.renny.perform(response,0)
        self.running = True # Same thing. Keep in mind, this will turn on the scheduled behaviour whenever a message is sent. Shouldn't really exist



    def saveLog(self,response):
        self.log = []
        
        # This code repeats, check that
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


    # This one is messy
    def update_menu(self):
        # Iterates through tkinter menues to update booleans
        for menu in self.menues:
            for boolean in menu.booleans:
                boolean[1].set(self.running)
        # Iterates pystray items to update booleans
        for i in range(len(self.background.checkables)):
            self.background.checkables[i] = self.running

    # Not even need the itep bitch, maybe not even the icon bitch
    def on_exit(self, icon, item):
        print("Closing application")
        self.root.destroy()
        icon.stop()






    #  __          ___           _                   
    #  \ \        / (_)         | |                  
    #   \ \  /\  / / _ _ __   __| | _____      _____ 
    #    \ \/  \/ / | | '_ \ / _` |/ _ \ \ /\ / / __|
    #     \  /\  /  | | | | | (_| | (_) \ V  V /\__ \
    #      \/  \/   |_|_| |_|\__,_|\___/ \_/\_/ |___/


    # Here the fun starts. Function takes the obj, which rn is either Chatbox or Console, and creates a window from it as a Toplevel
    def open_gui(self,obj):

        # Only if the window is not already opened
        if (obj.__name__) not in self.openWindows:

            self.background.icon.stop() # pystray needs to be stopped as it takes the main thread
            root = tk.Toplevel(self.root) # Needs to be Toplevel, or else the code gets messy and works weird, and also I don't even need the main root

            frame = obj(root) # Main frame, inside the toplevel. Remember our window modules are actually frames, as they are submodules of Frame

            menu = MenuCreator(root) # Adds te Options menu. Found it easier to add it to both
            menu.construct_menu(self.items)

            # TESTER. This button is naturally hidden in the Chatbox. Can be seen by extending the window
            tk.Button(frame,text="Force interaction",command=self.interactWithRenny).pack()

            print(f"{obj.__name__} opened")

            self.openWindows.append(obj.__name__) # Append this window's name to the list (we don't need to use the object)
            self.menues.append(menu) # Append the menu object (we do need to use it)

            root.protocol('WM_DELETE_WINDOW', lambda: self.withdraw_window(root,obj,menu)) # Hate this bitch


            # Yeah so, I need to initialize the Console log, and it has lot's of colours and stuff, so this is the best way I figured.
            # Prolly will need something similar for the chatbox, so it may be a good idea to keep it here
            try:
                frame.initialize(self.log)
            except AttributeError:
                print("what the heck")
            self.update_menu()

        else:
            print("Window already opened")



    def withdraw_window(self,root,obj,menu):
        
        root.destroy() # Destroy it idgaf
        self.openWindows.remove(obj.__name__)
        self.menues.remove(menu)

        # If there are no windows opened, kill all children from the main root
        # This is mainly needed because of the settings window, which is not included in the Windows list. I don't even remember why it wasn't a good idea
        # Won't question it in the foreseeable future
        if not self.openWindows:
            for child in self.root.winfo_children():
                if isinstance(child, tk.Toplevel):
                    child.destroy()
            self.background.setup_system_tray(self.items) # Also, when all windows are closed, start again the tray
        


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