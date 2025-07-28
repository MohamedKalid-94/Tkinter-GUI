import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Listbox")
root.geometry("300x250")

# Label for instruction
label = tk.Label(root, text="Select your favorite programming language:")
label.pack(pady=10)

# Create a Listbox
listbox = tk.Listbox(root, height=6, selectmode=tk.SINGLE)
languages = ["Python", "Java", "C++", "JavaScript", "Go", "Ruby"]

# Insert items into the Listbox
for lang in languages:
    listbox.insert(tk.END, lang)

listbox.pack(pady=10)

# Function to show the selected item
def show_selected():
    selected = listbox.get(listbox.curselection())
    result_label.config(text=f"You selected: {selected}")

# Button to trigger selection
button = tk.Button(root, text="Show Selection", command=show_selected)
button.pack(pady=5)

# Label to display selected item
result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the application
root.mainloop()
