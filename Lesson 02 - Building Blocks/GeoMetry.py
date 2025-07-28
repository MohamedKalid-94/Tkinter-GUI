from tkinter import *

root = Tk()
root.title("Geometry Managers - Grid")
root.geometry("300x150")

# All widgets here use only grid
Label(root, text="Grid Row 0, Column 0").grid(row=0, column=0)
Label(root, text="Grid Row 0, Column 1").grid(row=0, column=1)
Label(root, text="Grid Row 1, Column 0").grid(row=1, column=0)
Label(root, text="Grid Row 1, Column 1").grid(row=1, column=1)

root.mainloop()
