import threading
import time
import pystray
import tkinter as tk
from PIL import Image

class Background:
    
    def __init__(self, path):

        self.path = path

        #self.root = tk.Tk()

        self.text_types = [".txt",".pdf",".docx"]

        self.running = True


    def setup_daemon_thread(self, t, activity):
        # Create a thread for the daemon task
        daemon_thread = threading.Thread(target=activity, args=(t,))
        daemon_thread.daemon = True
        daemon_thread.start()


    def setup_system_tray(self,items):

        # Define the image to be shown in the system tray
        image = Image.open("images/icon.png")  # Replace with the path to your icon image

        menu = []

        for label, func, checkable, checked, default in items:
            if label == "SEPARATOR":
                menu.append(pystray.Menu.SEPARATOR)
            elif checkable:
                menu.append(pystray.MenuItem(label,func,checked=lambda item:checked))
            else:
                menu.append(pystray.MenuItem(label,func,default=default))
        


        # Create the system tray icon
        self.icon = pystray.Icon("Renny", image, "Renny", menu)
        self.icon.run()


if __name__ == "__main__":
    root = tk.Tk()
    background = Background("G:/Benja 2010")
    background.setup_system_tray([])
