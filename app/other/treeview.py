#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Choreado de https://recursospython.com/guias-y-manuales/vista-de-arbol-treeview-en-tkinter/
# I add local drives functionality
# I will leave original comments in spanish
# Benaj


import tkinter as tk
from tkinter import ttk,messagebox
from os import listdir, sep
from os.path import isdir, join, abspath
import win32api

class tv(ttk.Frame):
    
    def __init__(self, main_window):
        super().__init__(main_window)

        main_window.title("Select a folder")
        #main_window.title("Explorador de archivos y carpetas")
        
        self.header = ttk.Label(self, text="Select a folder to release Renny!")
        self.header.pack()

        self.treeview = ttk.Treeview(self)
        self.treeview.pack()
        
        # Asociar el evento de expansión de un elemento con la
        # función correspondiente.
        self.treeview.tag_bind("fstag", "<<TreeviewOpen>>", self.item_opened)
        
        # Expandir automáticamente.
        for w in (self, main_window):
            w.rowconfigure(0, weight=1)
            w.columnconfigure(0, weight=1)
        
        self.pack()
        
        # Este diccionario conecta los IDs de los ítems de Tk con
        # su correspondiente archivo o carpeta.
        self.fsobjects = {}
        
        self.file_image = tk.PhotoImage(file="file.png")
        self.folder_image = tk.PhotoImage(file="folder.png")
        

        # Load local drives
        self.load_drives()


        # Cargar el directorio raíz.
        #self.load_tree(abspath(sep))
        
        # Añadir el botón
        self.print_button = ttk.Button(self, text="Release Renny", command=self.releaseRenny)
        self.print_button.pack()
    
    def listdir(self, path):
        try:
            return listdir(path)
        except PermissionError:
            print("No tienes suficientes permisos para acceder a", path)
            return []
    
    def get_icon(self, path):
        """
        Retorna la imagen correspondiente según se especifique
        un archivo o un directorio.
        """
        return self.folder_image if isdir(path) else self.file_image
    
    def insert_item(self, name, path, parent=""):
        """
        Añade un archivo o carpeta a la lista y retorna el identificador
        del ítem.
        """
        iid = self.treeview.insert(parent, tk.END, text=name, tags=("fstag",), image=self.get_icon(path))
        self.fsobjects[iid] = path
        return iid
    
    def load_tree(self, path, parent=""):
        self.config(cursor="watch")
        self.update() 
        """
        Carga el contenido del directorio especificado y lo añade
        a la lista como ítemes hijos del ítem "parent".
        """
        for fsobj in self.listdir(path):
            fullpath = join(path, fsobj)
            child = self.insert_item(fsobj, fullpath, parent)
            if isdir(fullpath):
                for sub_fsobj in self.listdir(fullpath):
                    self.insert_item(sub_fsobj, join(fullpath, sub_fsobj), child)
        self.config(cursor="arrow")

        

    def load_drives(self, parent=""):

        drives = win32api.GetLogicalDriveStrings()
        drive_list = drives.split('\000')[:-1]  # Remove the last empty string

        for drive in drive_list:
            fullpath = drive
            child = self.insert_item(drive, drive, parent)
            if isdir(fullpath):
                for sub_fsobj in self.listdir(fullpath):
                    self.insert_item(sub_fsobj, join(fullpath, sub_fsobj), child)

    def load_subitems(self, iid):
        """
        Cargar el contenido de todas las carpetas hijas del directorio
        que se corresponde con el ítem especificado.
        """
        for child_iid in self.treeview.get_children(iid):
            if isdir(self.fsobjects[child_iid]):
                self.load_tree(self.fsobjects[child_iid], parent=child_iid)
    
    def item_opened(self, event):
        """
        Evento invocado cuando el contenido de una carpeta es abierto.
        """

        iid = self.treeview.selection()[0]
        self.load_subitems(iid)

    
    def releaseRenny(self):
        
        selected_item = self.treeview.selection()[0]
        selected_path = self.fsobjects[selected_item]
        print("Renny released at:", selected_path)
        messagebox.showinfo("Renny is free!",f"Renny released at:\n{selected_path}")
        return selected_path


if __name__ == "__main__":
    main_window = tk.Tk()
    app = tv(main_window)
    app.mainloop()
