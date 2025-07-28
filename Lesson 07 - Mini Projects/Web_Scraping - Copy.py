#Web Scraping + GUI
import tkinter as tk
import requests
from bs4 import BeautifulSoup

def get_price():
    res = requests.get("https://example.com")  # Replace with real URL
    soup = BeautifulSoup(res.text, 'html.parser')
    label.config(text=soup.title.string)

root = tk.Tk()
btn = tk.Button(root, text="Scrape", command=get_price)
btn.pack(pady=10)
label = tk.Label(root, text="Result Here")
label.pack()
root.mainloop()