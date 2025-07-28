from tkinter import *

root = Tk()
root.title("Scale Widget Example")

def show_value(val):
    label.config(text=f"Selected Value: {val}")

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=show_value)
scale.pack()

label = Label(root, text="Selected Value: 0")
label.pack()

root.mainloop()
