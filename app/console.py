import tkinter as tk

class Console(tk.Frame):

    def __init__(self,root,func,bg="black",fg="white"):
        super().__init__(root)

        root.geometry("600x500")

        root.title("Renny's behaviour")
        self.pack(side="top",fill="both",expand=True)

        self.bg = bg
        self.fg = fg

        self.header = tk.Label(self, text="Watch Renny's behaviour")
        self.header.pack()

        self.text =  tk.Text(self,state=tk.DISABLED,bg=self.bg,fg=self.fg)

        self.scrollbar = tk.Scrollbar(self,command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.text.pack(side="top",fill="both",expand=True)

        self.force_button = tk.Button(self,text="Force interaction",command=self.interact)
        self.force_button.pack(side="top")

        tk.Button(self,text="Retrieve History",command=self.checkHistory).pack()


    def checkHistory(self):
        
        try:
            with open("history.json", "r") as history:
                print(history)
        except FileNotFoundError:
            print("Not found")


    def interact(self):
        self.text.config(state=tk.NORMAL)
        self.text.insert(tk.END,"Add test text\n")
        self.text.yview_moveto(1.0)


    def colors(self,bg="black",fg="white"):
        self.bg=bg
        self.fg=fg

    def initialize(self,log):
        self.text.tag_configure("mind",foreground=self.fg)
        self.text.tag_configure("action",foreground="#33FA12")

        for i in log:
            keys = list(i.keys())
            mind = i['mind']
            action = keys[1]
            file = i[action]

            self.text.config(state=tk.NORMAL)
            self.text.insert(tk.END,f"-{mind}\n","mind")


            if action == "open-file":
                self.text.insert(tk.END,f"> He wants to check {file}\n\n","action")
            if action == "open-folder":
                self.text.insert(tk.END,f"> He wants to open {file}\n\n","action")
            if action == "keep-reading":
                self.text.insert(tk.END,f"> He wants to keep reading {file}\n\n","action")
            if action == "write-journal":
                self.text.insert(tk.END,f"> He wants to write on his journal\n\n","action")
            self.text.config(state=tk.DISABLED)

            self.text.yview_moveto(1.0)



if __name__ == "__main__":
    root = tk.Tk()
    Console(root)
    root.mainloop()