#PIL Image Viewer
import tkinter as tk
from PIL import Image, ImageTk

root = tk.Tk()
img = Image.open("example.jpg")  # Replace with a real image path
resized = img.resize((200, 200))
tkimg = ImageTk.PhotoImage(resized)
label = tk.Label(root, image=tkimg)
label.pack()
root.mainloop()