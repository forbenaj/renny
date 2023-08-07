import os
import chatbox as chatbox

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