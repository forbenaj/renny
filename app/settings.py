import tkinter as tk
import json

class SETTINGS(tk.Frame):

    def __init__(self,root):
        super().__init__(root)

        #root.geometry("400x200")

        #root.title("Settings")
        self.pack(side="top",fill="both",expand=True,padx=20,pady=20)

        self.settings = {"Token":"",
                         "CharID":"tDMVnZFsQxT33IY306y5Fia_AYhfqgx3ecUYIpo6ZWQ"
                         }

        TOKEN_LABEL      = tk.Label (self, text = "Token"        )
        TOKEN_LABEL .pack           (                            )
        self.TOKEN_INPUT = tk.Entry (self, justify = "center"    )
        self.TOKEN_INPUT .pack      (fill = "x", expand = True   )

        CHARA_LABEL      = tk.Label (self, text = "Character ID" )
        CHARA_LABEL .pack           (                            )
        self.CHARA_INPUT = tk.Entry (self, justify = "center"    )
        self.CHARA_INPUT .pack      (fill = "x", expand = True   )


        #tk.Button(self,text="Save",command=self.save_settings).pack()

    def load_settings(self):
        try:
            print("Loading settings...")
            with open("settings.cfg", "r") as settings_file:
                self.settings = json.loads(settings_file.read())
            print("Settings loaded")
        except FileNotFoundError:
            print("Not found")#. Creating save file...")
            #self.save_settings()
        
        self.TOKEN_INPUT.insert(0,self.settings["Token"])
        self.CHARA_INPUT.insert(0,self.settings["CharID"])


    def save_settings(self):
            with open("settings.cfg", "w") as settings_file:
                self.settings["Token"] = self.TOKEN_INPUT.get()
                self.settings["CharID"] = self.CHARA_INPUT.get()
                json.dump(self.settings,settings_file)
                print("Settings saved")
                #return self.settings


if __name__ == "__main__":
    root = tk.Tk()
    setup = SETTINGS(root)
    setup.load_settings()
    root.mainloop()