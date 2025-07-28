import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Radiobutton Widget")
root.geometry("300x200")

# Variable to store selected option
gender_var = tk.StringVar(value="None")

# Function to display the selected option
def show_selection():
    selected = gender_var.get()
    result_label.config(text=f"You selected: {selected}")

# Create Radiobuttons
radio_male = tk.Radiobutton(root, text="Male", variable=gender_var, value="Male", command=show_selection)
radio_female = tk.Radiobutton(root, text="Female", variable=gender_var, value="Female", command=show_selection)
radio_other = tk.Radiobutton(root, text="Other", variable=gender_var, value="Other", command=show_selection)

radio_male.pack(pady=5)
radio_female.pack(pady=5)
radio_other.pack(pady=5)

# Label to show the result
result_label = tk.Label(root, text="Select your gender")
result_label.pack(pady=10)

# Run the application
root.mainloop()
