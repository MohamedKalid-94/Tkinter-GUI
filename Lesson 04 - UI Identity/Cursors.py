from tkinter import *

root = Tk()
root.title("Cursor Demo")

button = Button(root, text="Click Me!", cursor="hand2")
button.pack(pady=20, padx=20)

root.mainloop()
