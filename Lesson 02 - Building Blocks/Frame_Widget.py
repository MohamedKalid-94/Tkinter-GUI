import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Widgets with Frame")
root.geometry("400x300")

# Create a Frame inside the main window
frame = tk.Frame(root, bd=2, relief="groove", padx=10, pady=10, bg="#f0f0f0")
frame.pack(pady=20)

# Add widgets inside the Frame
# Label
label = tk.Label(frame, text="Username:", font=("Arial", 12))
label.grid(row=0, column=0, pady=5, sticky="w")

# Entry
entry = tk.Entry(frame, width=25)
entry.grid(row=0, column=1, pady=5)

# Label 2
label2 = tk.Label(frame, text="Password:", font=("Arial", 12))
label2.grid(row=1, column=0, pady=5, sticky="w")

# Entry 2
entry2 = tk.Entry(frame, width=25, show="*")
entry2.grid(row=1, column=1, pady=5)

# Login Button
login_btn = tk.Button(frame, text="Login", bg="blue", fg="white", width=15)
login_btn.grid(row=2, columnspan=2, pady=10)

# Run the application
root.mainloop()
