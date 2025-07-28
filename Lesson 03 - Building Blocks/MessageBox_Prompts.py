#Messagebox and Desktop Prompts
import tkinter as tk
from tkinter import messagebox

def show_alert():
    messagebox.showinfo("Information", "This is a desktop prompt.")

root = tk.Tk()
tk.Button(root, text="Click Me", command=show_alert).pack(pady=20)
root.mainloop()