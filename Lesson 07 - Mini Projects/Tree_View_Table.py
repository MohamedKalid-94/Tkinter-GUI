#Treeview Table
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
tree = ttk.Treeview(root, columns=("Name", "Age"), show="headings")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.pack()

tree.insert("", "end", values=("John", 25))
tree.insert("", "end", values=("Alice", 30))

root.mainloop()