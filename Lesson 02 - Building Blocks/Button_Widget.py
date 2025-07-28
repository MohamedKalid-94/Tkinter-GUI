import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Button Widget")
root.geometry("300x200")

# Function to be called when button is clicked
def on_click():
    message_label.config(text="Button Clicked! 🎉")

# Create a Button widget
click_button = tk.Button(root, text="Click Me!", command=on_click)
click_button.pack(pady=20)

# Label to display the message
message_label = tk.Label(root, text="")
message_label.pack(pady=10)

# Run the application
root.mainloop()
