import tkinter as tk
from tkinter import ttk
from windows import set_dpi_awareness

import Data as d
import random 

secret_character = random.choice(d.characters)

set_dpi_awareness()

root = tk.Tk()
root.geometry("350x200")
root.resizable(False, False)
root.title("Game")


label = ttk.Label(root, text = secret_character, padding = 20)
label.config(font = ("Segoe UI", 20))
label.pack()

def refresh():
    secret_character = random.choice(d.characters)
    label["text"] = secret_character

buttons = ttk.Frame(root, padding = (20, 10))
buttons.pack()

refresh_button = ttk.Button(buttons, text = "Refresh", command = refresh)
refresh_button.pack(side = "left", fill = "x", expand = True)

root.mainloop()
































































