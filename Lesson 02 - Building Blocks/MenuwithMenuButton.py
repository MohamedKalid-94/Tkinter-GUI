import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Menubutton Example")
root.geometry("300x200")

# Create a Menubutton widget
menubtn = tk.Menubutton(root, text="Options", relief=tk.RAISED)
menubtn.grid(row=0, column=0, padx=20, pady=20)

# Create a Menu for the Menubutton
menu = tk.Menu(menubtn, tearoff=0)
menubtn.config(menu=menu)

# Add menu items
menu.add_command(label="New", command=lambda: print("New File"))
menu.add_command(label="Open", command=lambda: print("Open File"))
menu.add_separator()
menu.add_command(label="Exit", command=root.quit)

# Run the GUI loop
root.mainloop()
