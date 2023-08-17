import tkinter as tk
from app.utils.wids import Scroller

class Chatbox(tk.Frame):

    def __init__(self,root):
        super().__init__(root)
        
        root.geometry("560x460")

        self.chat_messages = Scroller(root)
        self.chat_messages.pack(fill="both",expand=1)
        self.chat_messages.config(bd=25,relief="sunken")


        self.message_box = tk.Frame(root)
        self.message_box.pack(side="bottom")

        self.message_input = tk.Text(self.message_box, width=40, height=10)
        self.message_input.pack(side="left",pady=5,padx=5)

        self.send_button = tk.Button(self.message_box,text="Send", width=15, height=2,background="green",foreground="white",command=self.sendMessage)
        self.send_button.pack(side="left",pady=5,padx=5)
        self.message_input.bind("<Return>",self.sendMessageEnter)

        self.receive_button = tk.Button(self.message_box,text="Receive", width=15, height=2,background="red",foreground="white",command=self.receiveMessage)
        self.receive_button.pack(side="left",pady=5,padx=5)
        tk.Frame(self.chat_messages.frame,width=450,bg="black").grid(column=0,columnspan=2)

        self.pack()

    def sendMessage(self):
        msg = self.message_input.get(1.0,tk.END).strip()
        if msg != "":
            new_message = tk.Label(self.chat_messages.frame, text=msg,bg="yellow",wraplength=233,pady=5,padx=5,relief="sunken")
            new_message.grid(column=1)
            self.message_input.delete(1.0,tk.END)
            self.chat_messages.updateScroller()
    
    def sendMessageEnter(self,event):
        if not event.state & 1:
            self.sendMessage()
            return "break"

    def receiveMessage(self):
        msg = "Tbd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24bd=24"
        new_message = tk.Label(self.chat_messages.frame, text=msg,bg="pink",wraplength=233,pady=5,padx=5,relief="sunken")
        new_message.grid(column=0)
        self.chat_messages.updateScroller()





if __name__ == "__main__":
    # Start the main loop
    root = tk.Tk()
    app = Chatbox(root)
    root.mainloop()
    print("start!")