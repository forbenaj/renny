import tkinter as tk
from wids import Scroller

class Comunicator:
    def __init__(self,root):

        self.root = root

        self.root.title("Communicator")
        self.root.geometry("400x500")

        '''raiz = tk.Tk()
        mi_Frame = tk.Frame() #Creacion del Frame
        mi_Frame.pack()  #Empaquetamiento del Frame
        mi_Frame.config(bg="blue") #cambiar color de fondo 
        mi_Frame.config(width="400", height="200") #cambiar tamaño
        mi_Frame.config(bd=24) #cambiar el grosor del borde
        mi_Frame.config(relief="sunken")   #cambiar el tipo de borde
        mi_Frame.config(cursor="heart")    #cambiar el tipo de cursor 
        raiz.mainloop()'''

        self.chat_messages = tk.Frame()
        self.chat_messages.pack()

        self.message_box = tk.Frame()
        self.message_box.pack(side="bottom",pady=20)

        # Create a label to display the entered text
        self.label = tk.Label(self.message_box, text="")
        self.label.pack()

        Scroller(self.root)

        # Create a text entry field
        self.text_entry = tk.Entry(self.message_box)
        self.text_entry.pack(side="left",pady=5)

        # Create a button to update the label with entered text
        self.send_button = tk.Button(self.message_box, text="Send", command=self.append_message)
        self.send_button.pack(side="left",pady=5)

        receive_button = tk.Button(self.message_box, text="Receive", command=self.appond_message)
        receive_button.pack(side="left",pady=5)


    def close_app(self,event):
        # Close the application
        root.destroy()


    def send_message(self):
        text = self.text_entry.get()
        self.label.config(text="Message: " + text)


    def append_message(self):
        msg = self.text_entry.get()
        #new_msg_sent = tk.Frame()
        #new_msg_sent.pack(side="top")
        new_label = tk.Label(self.chat_messages, text=msg)
        new_label.grid(column=0)

    def appond_message(self):
        msg = self.text_entry.get()
        #new_msg_sent = tk.Frame()
        #new_msg_sent.pack(side="top")
        new_label = tk.Label(self.chat_messages, text=msg)
        new_label.grid(column=1)

# Create the message window

if __name__ == "__main__":
    # Start the main loop
    root = tk.Tk()
    app = Comunicator(root)
    root.mainloop()
