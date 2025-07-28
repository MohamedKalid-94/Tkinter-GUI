import tkinter as tk

root = tk.Tk()
root.title("Place Example")
root.geometry("300x200")

tk.Label(root, text="Email:").place(x=20, y=30)
tk.Entry(root).place(x=80, y=30)

tk.Label(root, text="Phone:").place(x=20, y=70)
tk.Entry(root).place(x=80, y=70)

tk.Button(root, text="Submit").place(x=120, y=110)

root.mainloop()
