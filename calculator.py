#TODO: Button Functionality
#      Keyboard event handling
#      Change color of = button
#      Active operator button highlighted
#      Window resizing

import tkinter as tk
from tkinter import ttk, font, Frame, Button, Entry, N, W, E, S
from StdButton import *
from Integer import *
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

display = tk.StringVar(value="0")
numEntry = Entry(main, width=1, justify="right", font=("Helvetica 33"), textvariable=display, state="readonly")
numEntry.grid(column=0, row=0, sticky=(N, W, E), columnspan=5)
memory = Integer()
currentOperator = ""
saved = Integer(0)

StdButton(main, text="plch", command=lambda: reciprocal(display)).grid(column=1, row=1)
StdButton(main, text="plch", command=lambda: square(display)).grid(column=2, row=1)
StdButton(main, text="plch", command=lambda: square_root(display)).grid(column=3, row=1)
StdButton(main, text="⌫", command=lambda: backspace(display)).grid(column=4, row=1)
StdButton(main, text="MC", command=lambda: mem_clear(memory)).grid(column=0, row=2)
StdButton(main, text="MR", command=lambda: mem_recall(display, memory)).grid(column=1, row=2)
StdButton(main, text="M−", command=lambda: mem_subtract(display, memory)).grid(column=2, row=2)
StdButton(main, text="M+", command=lambda: mem_add(display, memory)).grid(column=3, row=2)
StdButton(main, text="÷", command=lambda: (currentOperator := divide(display, saved))).grid(column=4, row=2)
StdButton(main, text="%", command=lambda: percent(display)).grid(column=0, row=3)
StdButton(main, text="7", command=lambda: num_button(7, display, currentOperator)).grid(column=1, row=3)
StdButton(main, text="8", command=lambda: num_button(8, display, currentOperator)).grid(column=2, row=3)
StdButton(main, text="9", command=lambda: num_button(9, display, currentOperator)).grid(column=3, row=3)
StdButton(main, text="×", command=lambda: (currentOperator := multiply(display, saved))).grid(column=4, row=3)
StdButton(main, text="plch", command=lambda: plus_minus(display)).grid(column=0, row=4)
StdButton(main, text="4", command=lambda: num_button(4, display, currentOperator)).grid(column=1, row=4)
StdButton(main, text="5", command=lambda: num_button(5, display, currentOperator)).grid(column=2, row=4)
StdButton(main, text="6", command=lambda: num_button(6, display, currentOperator)).grid(column=3, row=4)
StdButton(main, text="−", command=lambda: (currentOperator := subtract(display, saved))).grid(column=4, row=4)
StdButton(main, text="C", command=lambda: temp_clear(display)).grid(column=0, row=5)
StdButton(main, text="1", command=lambda: num_button(1, display, currentOperator)).grid(column=1, row=5)
StdButton(main, text="2", command=lambda: num_button(2, display, currentOperator)).grid(column=2, row=5)
StdButton(main, text="3", command=lambda: num_button(3, display, currentOperator)).grid(column=3, row=5)
StdButton(main, text="+", command=lambda: (currentOperator := add(display, saved))).grid(column=4, row=5, rowspan=2, sticky=(N,S))
StdButton(main, text="AC", command=lambda: all_clear(display, memory)).grid(column=0, row=6)
StdButton(main, text="0", command=lambda: num_button(0, display, currentOperator)).grid(column=1, row=6)
StdButton(main, text=".", command=lambda: decimal).grid(column=2, row=6)
StdButton(main, text="=", command=lambda: equals(display, currentOperator)).grid(column=3, row=6)

root.mainloop()