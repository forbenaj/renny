import os
import app.chatbox as chatbox

# Dear sir, I would like to complain about that last tutorial about people not writing unit tests.
# I myself have coded all my life without testing 
# and... have... never... once... AAHHHH! [ImportError: attempted relative import with no known parent package]

def killRenny():
    try:
        os.remove('runn.ing')
        print("File deleted successfully.")
    except OSError as e:
        print(f"Error: {e}")

def main():

    with open('runn.ing', 'w') as file:
        file.write('Renny is running.')

    # Start the main loop
    root = chatbox.tk.Tk()
    app = chatbox.cb(root)
    root.mainloop()


    print("File created successfully.")
    


if __name__ == "__main__":
    main()