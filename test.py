import tkinter as tk


class Menu(tk.Frame):
    def __init__(self, root):
        super().__init__(root)

        root.title("Checkbutton Initialization Example")


        add_menu_button = tk.Button(self,text="Add menu",command=self.add_menu)
        add_menu_button.pack()
        add_menu_button2 = tk.Button(self,text="Kill Roy",command=self.kr)
        add_menu_button2.pack()
        add_menu_button3 = tk.Button(self,text="Add menu",command=self.add_menu)
        add_menu_button3.pack()

        self.pack()

    def add_menu(self):
        self.menu_bar = tk.Menu(root)
        root.config(menu=self.menu_bar)

        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        self.checkbutton_var = tk.BooleanVar()
        self.checkbutton_var.set(True)  # Set initial state to checked

        self.file_menu.add_checkbutton(label="Toggle Checkbutton", variable=self.checkbutton_var, command=self.toggle_checkbutton_state)
        self.file_menu.add_command(label="Add Item",command=self.add_item)

    def kr(self):
        self.destroy()

    def toggle_checkbutton_state(self):
        print("Checkbutton state:", self.checkbutton_var.get())

    def add_item(self):
        print("Item added")
        self.file_menu.add_checkbutton(label="Toggle Checkbutton 2", variable=self.checkbutton_var, command=self.toggle_checkbutton_state)
        #file_menu.add_command(label="Add Item",command=add_item)

if __name__ == "__main__":
    root = tk.Tk()
    menuer = Menu(root)
    root.mainloop()