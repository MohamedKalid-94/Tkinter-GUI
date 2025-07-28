from tkinter import *

root = Tk()
root.title("Anchor Demo")

label = Label(root, text="Top Left", anchor="nw", width=20, height=5, bg="yellow")
label.pack()

root.mainloop()
