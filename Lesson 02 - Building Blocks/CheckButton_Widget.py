import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Checkbutton Widget")
root.geometry("300x200")

# Variable to store the checkbox state
subscribe_var = tk.IntVar()

# Function to display the checkbox state
def show_status():
    if subscribe_var.get() == 1:
        result_label.config(text="You subscribed! ✅")
    else:
        result_label.config(text="You unsubscribed ❌")

# Create a Checkbutton widget
subscribe_check = tk.Checkbutton(root, text="Subscribe to newsletter", variable=subscribe_var, command=show_status)
subscribe_check.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

# Run the application
root.mainloop()
