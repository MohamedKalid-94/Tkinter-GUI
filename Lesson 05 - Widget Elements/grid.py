import tkinter as tk

root = tk.Tk()
root.title("Grid Example")
root.geometry("300x200")

tk.Label(root, text="Username").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Password").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root, show="*").grid(row=1, column=1, padx=10, pady=10)

tk.Button(root, text="Login").grid(row=2, columnspan=2, pady=10)

root.mainloop()
