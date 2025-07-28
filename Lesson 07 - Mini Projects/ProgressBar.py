#ProgressBar
import tkinter as tk
from tkinter import ttk
import time

root = tk.Tk()
progress = ttk.Progressbar(root, orient='horizontal', length=200, mode='determinate')
progress.pack(pady=20)

def start():
    for i in range(101):
        progress['value'] = i
        root.update()
        time.sleep(0.02)

btn = tk.Button(root, text="Start", command=start)
btn.pack()

root.mainloop()