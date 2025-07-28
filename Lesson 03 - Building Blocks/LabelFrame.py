# 📌 Grouping Labels with Labelframe
import tkinter as tk
root = tk.Tk()
labelframe = tk.LabelFrame(root, text="User Info", padx=10, pady=10)
labelframe.pack(padx=10, pady=10)
tk.Label(labelframe, text="Name:").grid(row=0, column=0)
tk.Entry(labelframe).grid(row=0, column=1)
tk.Label(labelframe, text="Email:").grid(row=1, column=0)
tk.Entry(labelframe).grid(row=1, column=1)
root.mainloop()
