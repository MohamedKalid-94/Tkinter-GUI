from tkinter import *
from tkinter import ttk

root = Tk()
root.title("ttk Widgets")

ttk.Label(root, text="This is a themed Label").pack(pady=5)
ttk.Button(root, text="Themed Button").pack(pady=5)

root.mainloop()
