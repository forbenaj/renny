import tkinter as tk

class Console():

    def __init__(self,root):

        self.root=root
        root.geometry("600x500")

        self.text =  tk.Text(self.root,state=tk.DISABLED,bg=self.bg,fg=self.fg)

        self.scrollbar = tk.Scrollbar(self.text,command=self.text.yview)
        self.text.config(yscrollcommand=self.scrollbar.set)

        self.scrollbar.pack(side="right", fill="y")
        self.text.pack(side="top",fill="both",expand=True)

        #test button
        tk.Button(self.root,text="test",command=self.testAddText).pack(side="top")


    def testAddText(self):
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