from tkinter import *

root = Tk()
root.title("Event Binding Example")

def on_key(event):
    label.config(text=f"Key Pressed: {event.char}")

label = Label(root, text="Press any key...")
label.pack(pady=20)

root.bind("<Key>", on_key)

root.mainloop()
