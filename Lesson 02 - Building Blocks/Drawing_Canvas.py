import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Canvas Drawing.")
root.geometry("400x400")

# Create a canvas widget
canvas = tk.Canvas(root, width=400, height=400, bg="white")
canvas.pack()

# Draw shapes on the canvas
# Draw a line
canvas.create_line(50, 50, 350, 50, fill="blue", width=3)

# Draw a rectangle
canvas.create_rectangle(50, 100, 200, 200, outline="green", width=2)

# Draw an oval (ellipse or circle)
canvas.create_oval(220, 100, 350, 200, fill="yellow", outline="black")

# Draw text
canvas.create_text(200, 250, text="Hello Canvas!", font=("Arial", 16), fill="red")

# Draw a polygon (triangle in this case)
canvas.create_polygon(100, 300, 150, 250, 200, 300, fill="purple")

# Run the application
root.mainloop()
