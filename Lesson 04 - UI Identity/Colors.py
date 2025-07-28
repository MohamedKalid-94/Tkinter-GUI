from tkinter import *

root = Tk()
root.title("Colors")

label = Label(root, text="Colored Label", bg="green", fg="white")
label.pack(padx=10, pady=10)

root.mainloop()
