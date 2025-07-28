from tkinter import *

root = Tk()
root.title("Fonts & Attention")

label = Label(root, text="Important Text", font=("Arial", 16, "bold italic"), fg="red")
label.pack(pady=20)

root.mainloop()
