import tkinter as tk

class Chatbox:

    def __init__(self,root):
        
        self.root = root
        self.root.geometry("500x400")


        self.main_frame = tk.Frame(root)
        self.main_frame.pack(fill="both",expand=1)

        self.my_canvas = tk.Canvas(self.main_frame)
        self.my_canvas.pack(side="left",fill="both",expand=1)

        self.my_scrollbar = tk.Scrollbar(self.main_frame,orient="vertical",command=self.my_canvas.yview)
        self.my_scrollbar.pack(side="right",fill="y")


        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>',lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
        self.my_canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        self.second_frame = tk.Frame(self.my_canvas)

        self.my_canvas.create_window((0,0),window=self.second_frame,anchor="nw")

        tk.Button(self.root,text="Create button",command=self.addButton).pack(side="bottom")


        self.message_box = tk.Frame(self.root)
        self.message_box.pack(side="bottom")

        self.message_input = tk.Text(self.message_box, width=40, height=10)
        self.message_input.pack(side="left",pady=5,padx=5)

        self.send_button = tk.Button(self.message_box,text="Send", width=15, height=2,background="green",foreground="white")
        self.send_button.pack(side="left",pady=5,padx=5)


    def addButton(self):
        
        tk.Button(self.second_frame,text=f"Button").pack(side="top")
        self.my_canvas.update_idletasks()
        self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all"))
        self.my_canvas.yview_moveto(1.0)


    def on_mousewheel(self,event):
        self.my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")


if __name__ == "__main__":
    # Start the main loop
    root = tk.Tk()
    app = Chatbox(root)
    root.mainloop()