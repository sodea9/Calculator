import tkinter as tk
from tkinter import font, Frame, Button, Entry, N, W, E, S
from StandardButton import *

root = tk.Tk()
root.title("Calculator")                            #TODO: fix weird button padding

main = Frame(root, padx=3, pady=3)
main.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Helvetica", size=20)

numEntry = Entry(main, justify="right", font=("Helvetica 30"))
numEntry.grid(column=0, row=0, sticky=(N, W, E), columnspan=5)

pixel = tk.PhotoImage(height=1, width=1)
StandardButton(main, image=pixel, text="plch").grid(column=1, row=1)
StandardButton(main, image=pixel, text="plch").grid(column=2, row=1)
StandardButton(main, image=pixel, text="plch").grid(column=3, row=1)
StandardButton(main, image=pixel, text="⌫").grid(column=4, row=1)
StandardButton(main, image=pixel, text="MC").grid(column=0, row=2)
StandardButton(main, image=pixel, text="MR").grid(column=1, row=2)
StandardButton(main, image=pixel, text="M−").grid(column=2, row=2)
StandardButton(main, image=pixel, text="M+").grid(column=3, row=2)
StandardButton(main, image=pixel, text="÷").grid(column=4, row=2)
StandardButton(main, image=pixel, text="%").grid(column=0, row=3)
StandardButton(main, image=pixel, text="7").grid(column=1, row=3)
StandardButton(main, image=pixel, text="8").grid(column=2, row=3)
StandardButton(main, image=pixel, text="9").grid(column=3, row=3)
StandardButton(main, image=pixel, text="×").grid(column=4, row=3)
StandardButton(main, image=pixel, text="plch").grid(column=0, row=4)
StandardButton(main, image=pixel, text="4").grid(column=1, row=4)
StandardButton(main, image=pixel, text="5").grid(column=2, row=4)
StandardButton(main, image=pixel, text="6").grid(column=3, row=4)
StandardButton(main, image=pixel, text="−").grid(column=4, row=4)
StandardButton(main, image=pixel, text="C").grid(column=0, row=5)
StandardButton(main, image=pixel, text="1").grid(column=1, row=5)
StandardButton(main, image=pixel, text="2").grid(column=2, row=5)
StandardButton(main, image=pixel, text="3").grid(column=3, row=5)
Button(main, width=BUTTONWIDTH, compound="c", image=pixel, text="+").grid(column=4, row=5, rowspan=2, sticky=(N,S))
StandardButton(main, image=pixel, text="AC").grid(column=0, row=6)
StandardButton(main, image=pixel, text="0").grid(column=1, row=6)
StandardButton(main, image=pixel, text=".").grid(column=2, row=6)
StandardButton(main, image=pixel, text="=").grid(column=3, row=6)

numEntry.focus()
root.mainloop()