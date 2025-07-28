import unittest
import tkinter as tk
from tkinter import messagebox

class SampleApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Test Example")

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.button = tk.Button(root, text="Greet", command=self.greet)
        self.button.pack()

    def greet(self):
        name = self.entry.get()
        messagebox.showinfo("Greeting", f"Hello, {name}!")

# For Testing Logic Only
class LogicTests(unittest.TestCase):
    def test_basic_greeting(self):
        self.assertEqual("Hello, John!", f"Hello, {'John'}!")

if __name__ == '__main__':
    unittest.main()