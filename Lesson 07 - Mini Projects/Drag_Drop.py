#Drag and Drop Example
import tkinter as tk

def on_drag(event):
    widget = event.widget
    widget.place(x=event.x_root - widget.winfo_width()//2, y=event.y_root - widget.winfo_height()//2)

root = tk.Tk()
root.geometry("400x300")

label = tk.Label(root, text="Drag Me", bg="skyblue", width=10)
label.place(x=50, y=50)
label.bind("<B1-Motion>", on_drag)

root.mainloop()