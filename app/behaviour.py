import tkinter as tk

class Console:

    def __init__(self,root,bg="black",fg="white"):

        self.root=root
        self.root.geometry("600x500")

        self.root.title("Renny's behaviour")

        self.bg = bg
        self.fg = fg

        self.header = tk.Label(self.root, text="Watch Renny's behaviour")
        self.header.pack()

        self.text =  tk.Text(self.root,state=tk.DISABLED,bg=self.bg,fg=self.fg)

        self.scrollbar = tk.Scrollbar(self.text,command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.text.pack(side="top",fill="both",expand=True)

        self.force_button = tk.Button(self.root,text="Force interaction",command=self.interact)
        self.force_button.pack(side="top")

        tk.Button(self.root,text="Retrieve History",command=self.checkHistory).pack()

    def checkHistory(self):
        
        try:
            with open("history.txt", "r") as history:
                print(history)
        except FileNotFoundError:
            print("Not found")

    def testAddText(self):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END,"Add test text\n")
        self.text.yview_moveto(1.0)

    def interact(self):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END,"Add test text\n")
        self.text.yview_moveto(1.0)


    def colors(self,bg="black",fg="white"):
        self.bg=bg
        self.fg=fg


if __name__ == "__main__":
    root = tk.Tk()
    Console(root)
    root.mainloop()