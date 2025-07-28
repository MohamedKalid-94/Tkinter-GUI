import tkinter as tk
from tkinter import ttk
from tkinter import filedialog, messagebox

root = tk.Tk()
root.title("Advanced Tkinter Widgets")
root.geometry("700x600")

# PanedWindow
paned = tk.PanedWindow(root)
paned.pack(fill=tk.BOTH, expand=1)
left = tk.Label(paned, text="Left Pane")
paned.add(left)
right = tk.Label(paned, text="Right Pane")
paned.add(right)

# Progressbar
progress = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate")
progress.pack(pady=10)
progress['value'] = 70  # Set initial value

# Treeview
tree = ttk.Treeview(root, columns=("Name", "Age"), show='headings')
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.insert("", "end", values=("Alice", 25))
tree.insert("", "end", values=("Bob", 30))
tree.pack(pady=10)

# Combobox
combo = ttk.Combobox(root, values=["Python", "Java", "C++"])
combo.set("Choose Language")
combo.pack(pady=10)

# Notebook (Tabs)
notebook = ttk.Notebook(root)
tab1 = ttk.Frame(notebook)
tab2 = ttk.Frame(notebook)
notebook.add(tab1, text='Tab 1')
notebook.add(tab2, text='Tab 2')
notebook.pack(pady=10)
tk.Label(tab1, text="Welcome to Tab 1").pack(pady=10)
tk.Label(tab2, text="Welcome to Tab 2").pack(pady=10)

# Tooltip (Custom Implementation)
def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.withdraw()
    tooltip.overrideredirect(True)
    label = tk.Label(tooltip, text=text, bg="yellow", relief="solid", borderwidth=1)
    label.pack()

    def enter(event):
        tooltip.deiconify()
        tooltip.geometry(f"+{event.x_root+10}+{event.y_root+10}")

    def leave(event):
        tooltip.withdraw()

    widget.bind("<Enter>", enter)
    widget.bind("<Leave>", leave)

btn = tk.Button(root, text="Hover over me")
btn.pack(pady=10)
create_tooltip(btn, "This is a tooltip!")

# Keyboard Shortcuts
root.bind("<Control-s>", lambda e: messagebox.showinfo("Save", "Ctrl+S Pressed"))
root.bind("<Control-q>", lambda e: root.quit())

# Clock (Animation using after)
clock_label = tk.Label(root, font=('Arial', 14))
clock_label.pack(pady=10)

def update_time():
    import time
    clock_label.config(text=time.strftime("%H:%M:%S"))
    root.after(1000, update_time)

update_time()

# File Dialog
file_button = tk.Button(root, text="Open File", command=lambda: filedialog.askopenfilename())
file_button.pack(pady=10)

root.mainloop()
