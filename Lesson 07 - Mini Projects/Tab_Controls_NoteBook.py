#Tab Controls with ttk.Notebook
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
notebook = ttk.Notebook(root)
notebook.pack(padx=10, pady=10, fill='both', expand=True)

frame1 = ttk.Frame(notebook)
frame2 = ttk.Frame(notebook)
notebook.add(frame1, text='Tab 1')
notebook.add(frame2, text='Tab 2')

tk.Label(frame1, text='This is Tab 1').pack()
tk.Label(frame2, text='This is Tab 2').pack()

root.mainloop()