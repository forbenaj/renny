from app.console import Console
from app.chatbox import Chatbox
import pystray
from PIL import Image
import tkinter as tk
import time


class Renny:

    def __init__(self,root):

        self.root = root
        self.running=True
        self.windows = []

        #                Label                  Func                Checkable?           Checked?           Default?   
        self.items = [("Open communicator",    self.communicator,      False,              None,             True),
                      ("See activity",         self.see_activity,      False,              None,             False),]
        


    def run(self):
        self.mainframe = tk.Frame(self.root)
        self.mainframe.pack()
        tk.Button(self.mainframe,text="Next",width=40,height=10,command=self.firstTime).pack()
        self.root.mainloop()



    def firstTime(self):
        self.mainframe.destroy()
        self.root.withdraw()
        

        self.setup_system_tray(self.items)

    def open_gui(self,window):
        self.icon.stop()
        if window == "chatbox":
            self.communicator()
        elif window == "console":
            self.see_activity()


    def communicator(self):
        
        self.chatbox_root = self.root if self.windows == [] else tk.Toplevel(self.root)
        self.construct_menu(self.chatbox_root)
        print("Communicator opened")
        self.chatbox = Chatbox(self.chatbox_root)
        tk.Button(self.chatbox,text="kill",command=self.kill_chatbox).pack()
        self.windows.append(self.chatbox)
        print(f"This is {self.chatbox}")
        self.chatbox_root.protocol('WM_DELETE_WINDOW', self.kill_chatbox)
        self.chatbox_root.after(100, self.chatbox_root.deiconify)



    def see_activity(self):
        self.console_root = self.root if self.windows == [] else tk.Toplevel(self.root)
        self.construct_menu(self.console_root)
        print("Behaviour opened")
        self.console = Console(self.console_root)
        tk.Button(self.console,text="kill",command=self.kill_console).pack()
        self.windows.append(self.console)
        print(f"This is {self.console}")
        self.console_root.protocol('WM_DELETE_WINDOW', self.kill_console)
        self.console_root.after(100, self.console_root.deiconify)





    def withdraw_window(self,window,root):
        window.destroy()
        root.withdraw()
        self.windows.remove(window)
        if not self.windows:
            self.setup_system_tray(self.items)


    def kill_chatbox(self):
        self.chatbox.destroy()
        self.chatbox_root.withdraw()
        self.windows.remove(self.chatbox)
        if not self.windows:
            self.setup_system_tray(self.items)

    def kill_console(self):
        self.console.destroy()
        self.console_root.withdraw()
        self.windows.remove(self.console)
        if not self.windows:
            self.setup_system_tray(self.items)

    def setup_system_tray(self,items):

        # Define the image to be shown in the system tray
        image = Image.open("images/icon.png")  # Replace with the path to your icon image

        menu = [pystray.MenuItem("Chatbox",lambda:self.open_gui("chatbox"),default=True),
                pystray.MenuItem("Console",lambda:self.open_gui("console"))]


        # Create the system tray icon
        self.icon = pystray.Icon("Renny", image, "Renny", menu)
        self.icon.run()
    
    def construct_menu(self,root):
        
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)
        self.options_menu = tk.Menu(self.menu_bar, tearoff=0)
        
        self.menu_bar.add_cascade(label="Options", menu=self.options_menu)
        
        self.options_menu.add_command(label="Chatbox", command=self.communicator)
        self.options_menu.add_command(label="Console", command=self.see_activity)

        

if __name__ == "__main__":
    root = tk.Tk()
    renny = Renny(root)
    renny.run()