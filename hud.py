import tkinter as tk

def close_app(event):
    # Close the application
    root.destroy()


def send_message():
    text = text_entry.get()
    label.config(text="Message: " + text)


def append_message():
    msg = text_entry.get()
    #new_msg_sent = tk.Frame()
    #new_msg_sent.pack(side="top")
    new_label = tk.Label(chat_messages, text=msg)
    new_label.grid(column=0)

def appond_message():
    msg = text_entry.get()
    #new_msg_sent = tk.Frame()
    #new_msg_sent.pack(side="top")
    new_label = tk.Label(chat_messages, text=msg)
    new_label.grid(column=1)


# Create the message window
root = tk.Tk()
root.title("Communicator")


root.geometry("400x500")

'''raiz = tk.Tk()
mi_Frame = tk.Frame() #Creacion del Frame
mi_Frame.pack()  #Empaquetamiento del Frame
mi_Frame.config(bg="blue") #cambiar color de fondo 
mi_Frame.config(width="400", height="200") #cambiar tamaño
mi_Frame.config(bd=24) #cambiar el grosor del borde
mi_Frame.config(relief="sunken")   #cambiar el tipo de borde
mi_Frame.config(cursor="heart")    #cambiar el tipo de cursor 
raiz.mainloop()'''

chat_messages = tk.Frame()
chat_messages.pack()

message_box = tk.Frame()
message_box.pack(side="bottom",pady=20)

# Create a label to display the entered text
label = tk.Label(message_box, text="")
label.pack()

# Create a text entry field
text_entry = tk.Entry(message_box)
text_entry.pack(side="left",pady=5)

# Create a button to update the label with entered text
send_button = tk.Button(message_box, text="Send", command=append_message)
send_button.pack(side="left",pady=5)

receive_button = tk.Button(message_box, text="Receive", command=appond_message)
receive_button.pack(side="left",pady=5)

# Start the main loop
root.mainloop()
