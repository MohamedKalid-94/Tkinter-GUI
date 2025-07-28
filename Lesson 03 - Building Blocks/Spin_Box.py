from tkinter import *

root = Tk()
root.title("Spinbox Widget Example")

spin = Spinbox(root, from_=1, to=10)
spin.pack()

root.mainloop()
