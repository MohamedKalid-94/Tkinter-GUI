from tkinter import *

root = Tk()
root.title("Text Widget Example")

text = Text(root, height=5, width=30)
text.pack()

text.insert(END, "Type something here...")

root.mainloop()
