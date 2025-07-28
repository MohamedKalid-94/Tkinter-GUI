import tkinter as tk

root = tk.Tk()
root.title("Pack Example")
root.geometry("300x200")

label = tk.Label(root, text="Welcome!", bg="lightblue")
label.pack(pady=10)

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Submit")
button.pack(pady=10)

root.mainloop()
