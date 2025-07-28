import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Label Widget")
root.geometry("300x150")

# Create a Label widget
greeting_label = tk.Label(root, text="Welcome to Tkinter!", font=("Helvetica", 14), fg="blue")
greeting_label.pack(pady=20)  # Add some padding vertically

# Run the application
root.mainloop()
