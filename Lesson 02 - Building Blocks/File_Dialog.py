from tkinter import *
from tkinter import filedialog

root = Tk()
root.title("File Dialog Example")

def open_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        label.config(text=f"Selected: {file_path}")

Button(root, text="Open File", command=open_file).pack()
label = Label(root, text="No file selected")
label.pack()

root.mainloop()
