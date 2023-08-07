import threading
import time
import pystray
from PIL import Image

index = 0

def doSomething(t):
    while True:
        print("Doing something...")
        time.sleep(t)

def on_exit(icon, item):
    print("Closing application")
    icon.stop()

def communicator():
    print("Communicator opened")

def find():
    print("Opening folder")

def setup_system_tray(t):
    # Create a thread for the daemon task
    daemon_thread = threading.Thread(target=doSomething,args=(t,))
    daemon_thread.daemon = True
    daemon_thread.start()


    # Define the image to be shown in the system tray
    image = Image.open("icon.png")  # Replace with the path to your icon image

    # Create the system tray icon
    menu = pystray.Menu(pystray.MenuItem("Chat", communicator),
                        pystray.MenuItem("Find", find),
                        pystray.Menu.SEPARATOR,
                        pystray.MenuItem("Exit", on_exit))
    icon = pystray.Icon("Renny", image, "Renny", menu)
    icon.run()

if __name__ == "__main__":
    setup_system_tray(1)