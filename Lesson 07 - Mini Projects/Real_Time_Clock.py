#Real-Time Clock
import tkinter as tk
from time import strftime

def update_clock():
    time_string = strftime('%H:%M:%S')
    clock_label.config(text=time_string)
    clock_label.after(1000, update_clock)

root = tk.Tk()
root.title("Real-Time Clock")
root.geometry("250x100")

clock_label = tk.Label(root, font=('Arial', 40), fg='blue')
clock_label.pack()

update_clock()
root.mainloop()
