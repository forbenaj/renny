import tkinter as tk

class Scroller(tk.Frame):

    def __init__(self, master):

        super().__init__(master)

        self.pack(fill="both",expand=True)

        self.my_canvas = tk.Canvas(self)
        self.my_canvas.pack(side="left",fill="both",expand=1)

        self.my_scrollbar = tk.Scrollbar(self,orient="vertical",command=self.my_canvas.yview)
        self.my_scrollbar.pack(side="right",fill="y")


        self.my_canvas.configure(yscrollcommand=self.my_scrollbar.set)
        self.my_canvas.bind('<Configure>',lambda e: self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all")))
        self.my_canvas.bind_all("<MouseWheel>", self.on_mousewheel)

        self.frame = tk.Frame(self.my_canvas)
        self.frame.pack(fill="both",expand=1)

        self.my_canvas.create_window((0, 0), window=self.frame, anchor="nw")


    def updateScroller(self):
        self.my_canvas.update_idletasks()
        self.my_canvas.configure(scrollregion=self.my_canvas.bbox("all"))
        self.my_canvas.yview_moveto(1.0)


    def on_mousewheel(self,event):
        self.my_canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")



if __name__ == "__main__":
    # Start the main loop
    root = tk.Tk()
    app = Scroller(root)
    root.mainloop()