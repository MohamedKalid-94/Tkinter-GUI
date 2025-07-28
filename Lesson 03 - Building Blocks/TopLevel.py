from tkinter import *

root = Tk()
root.title("Main Window")

def open_window():
    top = Toplevel(root)
    top.title("New Window")
    Label(top, text="This is a Toplevel window").pack()

Button(root, text="Open New Window", command=open_window).pack()

root.mainloop()
