import os
import app.chatbox as chatbox

# Dear sir, I would like to complain about that last tutorial about people not writing unit tests.
# I myself have coded all my life without testing 
# and... have... never... once... AAHHHH! [ImportError: attempted relative import with no known parent package]

desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

def firstTime():
    pass

def save_config():
    config_data = {
        "path": "",
        "other": ""
    }

    #file_path = os.path.join(desktop, "config.cfg")
    with open("config.cfg", "w") as config_file:
        config_file.write(path)
        #json.dump(config_data, config_file)

def load_config():
    try:
        #file_path = os.path.join(desktop, "config.cfg")  # Use the same file_path used in save_config()
        
        with open("config.cfg", "r") as config_file:
            path=config_file.read()


    except FileNotFoundError:
        path = ""

    return path

def killRenny():
    try:
        os.remove('runn.ing')
        print("File deleted successfully.")
    except OSError as e:
        print(f"Error: {e}")

def main(path):

    
    with open('runn.ing', 'w') as file:
        file.write('Renny is running.')

    # Start the main loop
    root = chatbox.tk.Tk()
    app = chatbox.cb(root)
    root.mainloop()


    print("File created successfully.")
    


if __name__ == "__main__":
    path=load_config()
    if path == "":
        firstTime()
    else:
        main(path)