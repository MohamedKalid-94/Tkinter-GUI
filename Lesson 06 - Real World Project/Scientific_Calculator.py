import tkinter as tk
import math

def click(event):
    text = event.widget["text"]
    if text == "=":
        try:
            expression = entry.get().replace("^", "**")
            result = str(eval(expression))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    elif text == "C":
        entry.delete(0, tk.END)
    elif text in functions:
        try:
            val = float(entry.get())
            result = str(functions[text](val))
            entry.delete(0, tk.END)
            entry.insert(tk.END, result)
        except Exception:
            entry.delete(0, tk.END)
            entry.insert(tk.END, "Error")
    else:
        entry.insert(tk.END, text)

# Scientific functions
functions = {
    "sin": lambda x: round(math.sin(math.radians(x)), 5),
    "cos": lambda x: round(math.cos(math.radians(x)), 5),
    "tan": lambda x: round(math.tan(math.radians(x)), 5),
    "log": lambda x: round(math.log10(x), 5),
    "ln": lambda x: round(math.log(x), 5),
    "√": lambda x: round(math.sqrt(x), 5),
    "x²": lambda x: round(math.pow(x, 2), 5)
}

root = tk.Tk()
root.title("Scientific Calculator")
root.geometry("400x600")
root.resizable(False, False)

entry = tk.Entry(root, font=("Arial", 20), justify="right", bd=10, relief=tk.RIDGE)
entry.pack(fill=tk.BOTH, ipadx=8, ipady=15, padx=10, pady=10)

btn_frame = tk.Frame(root)
btn_frame.pack()

# Scientific function buttons
sci_buttons = ["sin", "cos", "tan", "log", "ln", "√", "x²"]

frame1 = tk.Frame(btn_frame)
frame1.pack()
for btn_text in sci_buttons:
    btn = tk.Button(frame1, text=btn_text, font=("Arial", 16), width=6)
    btn.pack(side="left", padx=2, pady=2)
    btn.bind("<Button-1>", click)

# Numeric and operator buttons
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "^", "+"],
    ["C", "=", "(", ")"]
]

for row in buttons:
    frame = tk.Frame(btn_frame)
    frame.pack()
    for btn_text in row:
        btn = tk.Button(frame, text=btn_text, font=("Arial", 16), width=6)
        btn.pack(side="left", padx=2, pady=2)
        btn.bind("<Button-1>", click)

root.mainloop()
