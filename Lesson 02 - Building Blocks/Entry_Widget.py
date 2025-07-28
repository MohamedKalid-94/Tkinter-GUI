import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Entry Widget")
root.geometry("300x200")

# Create a label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create an Entry widget
name_entry = tk.Entry(root, width=30)
name_entry.pack(pady=5)

# Function to show the entered name
def show_name():
    entered_name = name_entry.get()
    result_label.config(text=f"Hello, {entered_name}!")

# Button to submit
submit_button = tk.Button(root, text="Submit", command=show_name)
submit_button.pack(pady=10)

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
