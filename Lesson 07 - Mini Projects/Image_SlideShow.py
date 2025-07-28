# Image Slideshow
import tkinter as tk
from PIL import Image, ImageTk
import os

root = tk.Tk()
root.geometry("300x300")
img_files = ["img1.png", "img2.png"]  # Add your own image paths
imgs = [ImageTk.PhotoImage(Image.open(img)) for img in img_files]

label = tk.Label(root)
label.pack()

index = 0
def next_img():
    global index
    index = (index + 1) % len(imgs)
    label.config(image=imgs[index])
    root.after(1000, next_img)

label.config(image=imgs[0])
root.after(1000, next_img)
root.mainloop()