from tkinter import *

root = Tk()
root.title("Relief Styles")

styles = ["flat", "sunken", "raised", "groove", "ridge"]
for style in styles:
    Label(root, text=style, relief=style, borderwidth=4, width=20).pack(pady=5)

root.mainloop()
