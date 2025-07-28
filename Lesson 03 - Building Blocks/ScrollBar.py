from tkinter import *

root = Tk()
root.title("Scrollbar Example")

text = Text(root, wrap=NONE)
text.pack(side=LEFT)

scroll = Scrollbar(root, command=text.yview)
scroll.pack(side=RIGHT, fill=Y)

text.config(yscrollcommand=scroll.set)

root.mainloop()
