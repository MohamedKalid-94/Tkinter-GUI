#Form Validation + Submission
import tkinter as tk
from tkinter import messagebox

def submit():
    name = entry_name.get()
    age = entry_age.get()
    if not name:
        messagebox.showwarning("Validation Error", "Name cannot be empty")
        return
    if not age.isdigit():
        messagebox.showwarning("Validation Error", "Age must be a number")
        return
    messagebox.showinfo("Success", f"Submitted:\nName: {name}\nAge: {age}")

root = tk.Tk()
root.title("Form Submission")
root.geometry("300x200")

tk.Label(root, text="Name:").pack(pady=5)
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

tk.Label(root, text="Age:").pack(pady=5)
entry_age = tk.Entry(root)
entry_age.pack(pady=5)

submit_btn = tk.Button(root, text="Submit", command=submit)
submit_btn.pack(pady=20)

root.mainloop()