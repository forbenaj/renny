import tkinter as tk
import pygame


def toggle_fullscreen(event):
    # Toggle fullscreen mode
    root.attributes('-fullscreen', not root.attributes('-fullscreen'))

def close_app(event):
    # Close the application
    root.destroy()


def send_message():
    text = text_entry.get()
    label.config(text="Message: " + text)


# Create the main application window
root = tk.Tk()
root.title("Fullscreen App")

# Bind the F11 key to toggle fullscreen mode
root.bind("<F11>", toggle_fullscreen)

# Bind the Escape key to close the application
root.bind("<Escape>", close_app)

# Set fullscreen mode initially to False
root.attributes('-fullscreen', False)

# Create the message window
msg = tk.Tk()
msg.title("Communicator")


# Create a text entry field
text_entry = tk.Entry(msg)
text_entry.pack(pady=5)

# Create a label to display the entered text
label = tk.Label(msg, text="")
label.pack()

# Create a button to update the label with entered text
update_button = tk.Button(msg, text="Update Text", command=send_message)
update_button.pack()

msg.geometry("300x100")


# Start the main loop
msg.mainloop()
