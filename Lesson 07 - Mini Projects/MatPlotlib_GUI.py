#Matplotlib Integration
import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()
fig = Figure(figsize=(4, 3), dpi=100)
plot = fig.add_subplot(111)
plot.plot([1, 2, 3, 4], [10, 20, 25, 30])
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().pack()
root.mainloop()