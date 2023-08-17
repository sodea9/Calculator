#TODO: Button Functionality
#      Input handling
#      Keyboard event handling
#      Change color of = button

import tkinter as tk
from tkinter import ttk, font, Frame, Button, Entry, N, W, E, S
from StdButton import *
from buttonfunctions import *

root = tk.Tk()
root.title("Calculator")
icon = tk.PhotoImage(file="calcicon.png")
root.iconphoto(False, icon)

main = Frame(root, padx=3, pady=3)
main.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

s = ttk.Style(root)
s.theme_use("xpnative")
#print(root.get_themes())
#print(s.theme_names())

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Helvetica", size=20)

display = tk.StringVar()
numEntry = Entry(main, width=1, justify="right", font=("Helvetica 33"), textvariable=display)
numEntry.grid(column=0, row=0, sticky=(N, W, E), columnspan=5)

StdButton(main, text="plch").grid(column=1, row=1)
StdButton(main, text="plch").grid(column=2, row=1)
StdButton(main, text="plch").grid(column=3, row=1)
StdButton(main, text="⌫", command=lambda: backspace(display)).grid(column=4, row=1)
StdButton(main, text="MC").grid(column=0, row=2)
StdButton(main, text="MR").grid(column=1, row=2)
StdButton(main, text="M−").grid(column=2, row=2)
StdButton(main, text="M+").grid(column=3, row=2)
StdButton(main, text="÷").grid(column=4, row=2)
StdButton(main, text="%").grid(column=0, row=3)
StdButton(main, text="7", command=lambda: num_button(7, display)).grid(column=1, row=3)
StdButton(main, text="8", command=lambda: num_button(8, display)).grid(column=2, row=3)
StdButton(main, text="9", command=lambda: num_button(9, display)).grid(column=3, row=3)
StdButton(main, text="×").grid(column=4, row=3)
StdButton(main, text="plch").grid(column=0, row=4)
StdButton(main, text="4", command=lambda: num_button(4, display)).grid(column=1, row=4)
StdButton(main, text="5", command=lambda: num_button(5, display)).grid(column=2, row=4)
StdButton(main, text="6", command=lambda: num_button(6, display)).grid(column=3, row=4)
StdButton(main, text="−").grid(column=4, row=4)
StdButton(main, text="C").grid(column=0, row=5)
StdButton(main, text="1", command=lambda: num_button(1, display)).grid(column=1, row=5)
StdButton(main, text="2", command=lambda: num_button(2, display)).grid(column=2, row=5)
StdButton(main, text="3", command=lambda: num_button(3, display)).grid(column=3, row=5)
StdButton(main, text="+").grid(column=4, row=5, rowspan=2, sticky=(N,S))
StdButton(main, text="AC").grid(column=0, row=6)
StdButton(main, text="0", command=lambda: num_button(0, display)).grid(column=1, row=6)
StdButton(main, text=".").grid(column=2, row=6)
StdButton(main, text="=").grid(column=3, row=6)

numEntry.focus()
root.mainloop()