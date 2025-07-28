from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Messagebox Example")

def show_msg():
    messagebox.showinfo("Greeting", "Hello, Tkinter!")

Button(root, text="Click Me", command=show_msg).pack()

root.mainloop()
