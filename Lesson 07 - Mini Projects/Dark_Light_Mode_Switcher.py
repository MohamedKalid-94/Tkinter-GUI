#Dark/Light Mode Switcher
import tkinter as tk

def toggle_mode():
    if root['bg'] == 'white':
        root.config(bg='black')
        label.config(bg='black', fg='white')
        toggle_btn.config(text='Switch to Light Mode', bg='gray', fg='white')
    else:
        root.config(bg='white')
        label.config(bg='white', fg='black')
        toggle_btn.config(text='Switch to Dark Mode', bg='lightgray', fg='black')

root = tk.Tk()
root.title("Dark/Light Mode Switcher")
root.geometry("300x200")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 16))
label.pack(pady=30)

toggle_btn = tk.Button(root, text="Switch to Dark Mode", command=toggle_mode)
toggle_btn.pack()

root.mainloop()