# 📌 Multiple Lines with Message Widget
import tkinter as tk
root = tk.Tk()
message = tk.Message(root, text="This is a multiline message box that automatically wraps text.", width=200)
message.pack(padx=10, pady=10)
root.mainloop()
