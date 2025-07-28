from tkinter import *

root = Tk()
root.title("Bitmap Demo")

label = Label(root, bitmap="info")
label.pack(padx=20, pady=20)

root.mainloop()
