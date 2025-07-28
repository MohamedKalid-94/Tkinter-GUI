from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Form Submission")

def submit_form():
    name = entry.get()
    if name.strip() == "":
        messagebox.showwarning("Validation", "Name field is required!")
    else:
        messagebox.showinfo("Success", f"Submitted: {name}")

Label(root, text="Enter your name:").pack()
entry = Entry(root)
entry.pack()

Button(root, text="Submit", command=submit_form).pack()

root.mainloop()
