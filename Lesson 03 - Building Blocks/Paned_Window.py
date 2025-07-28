# 📌 Dividing with Panes (PanedWindow)
import tkinter as tk
root = tk.Tk()
pane = tk.PanedWindow(root, orient='horizontal')
pane.pack(fill='both', expand=True)
pane.add(tk.Label(pane, text="Left Pane"))
pane.add(tk.Label(pane, text="Right Pane"))
root.mainloop()