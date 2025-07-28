import tkinter as tk
from tkinter import messagebox

# Function for menu commands
def new_file():
    messagebox.showinfo("New File", "Creating a new file...")

def open_file():
    messagebox.showinfo("Open File", "Opening a file...")

def exit_app():
    root.quit()

# Create the main window
root = tk.Tk()
root.title("Menu Example")
root.geometry("400x300")

# Create the menu bar
menu_bar = tk.Menu(root)

# Create a File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# Add File menu to the menu bar
menu_bar.add_cascade(label="File", menu=file_menu)

# Create a Help menu
help_menu = tk.Menu(menu_bar, tearoff=0)
help_menu.add_command(label="About", command=lambda: messagebox.showinfo("About", "Tkinter Menu Example"))

# Add Help menu to the menu bar
menu_bar.add_cascade(label="Help", menu=help_menu)

# Set the menu bar to the window
root.config(menu=menu_bar)

# Run the app
root.mainloop()
