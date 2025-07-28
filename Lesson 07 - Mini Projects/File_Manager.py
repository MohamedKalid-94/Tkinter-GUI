import tkinter as tk
from tkinter import filedialog, messagebox, ttk
import os

class FileManager:
    def __init__(self, root):
        self.root = root
        self.root.title("File Explorer")

        self.tree = ttk.Treeview(root)
        self.tree.pack(expand=True, fill='both')

        tk.Button(root, text="Open Folder", command=self.open_folder).pack()

    def open_folder(self):
        folder = filedialog.askdirectory()
        if folder:
            self.tree.delete(*self.tree.get_children())
            self.insert_items('', folder)

    def insert_items(self, parent, path):
        for item in os.listdir(path):
            abspath = os.path.join(path, item)
            oid = self.tree.insert(parent, 'end', text=item, open=False)
            if os.path.isdir(abspath):
                self.insert_items(oid, abspath)

root = tk.Tk()
FileManager(root)
root.mainloop()