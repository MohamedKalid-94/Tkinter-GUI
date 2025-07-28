#Tooltip on Hover
import tkinter as tk

class ToolTip:
    def __init__(self, widget, text):
        self.widget = widget
        self.text = text
        widget.bind("<Enter>", self.show_tip)
        widget.bind("<Leave>", self.hide_tip)

    def show_tip(self, event):
        self.tip = tk.Toplevel(self.widget)
        self.tip.wm_overrideredirect(True)
        self.tip.geometry(f"+{event.x_root + 10}+{event.y_root + 10}")
        label = tk.Label(self.tip, text=self.text, bg="yellow")
        label.pack()

    def hide_tip(self, event):
        self.tip.destroy()

root = tk.Tk()
btn = tk.Button(root, text="Click Me")
btn.pack(pady=20)
ToolTip(btn, "This is a tooltip")

root.mainloop()