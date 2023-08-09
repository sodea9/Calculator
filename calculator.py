import tkinter as tk
from tkinter import ttk, N, W, E, S
from PIL import ImageTk, Image

root = tk.Tk()
root.title("Calculator")

main = ttk.Frame(root, padding = 3)
main.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

numEntry = ttk.Entry(main, justify="right", font=("10"))
numEntry.grid(column=0, row=0, sticky=(N, W, E), columnspan=5)

ttk.Button(main, text="plch").grid(column=1, row=1)
ttk.Button(main, text="plch").grid(column=2, row=1)
ttk.Button(main, text="plch").grid(column=3, row=1)
ttk.Button(main, text="⌫").grid(column=4, row=1)
ttk.Button(main, text="MC").grid(column=0, row=2)
ttk.Button(main, text="MR").grid(column=1, row=2)
ttk.Button(main, text="M-").grid(column=2, row=2)
ttk.Button(main, text="M+").grid(column=3, row=2)
ttk.Button(main, text="÷").grid(column=4, row=2)
ttk.Button(main, text="%").grid(column=0, row=3)
ttk.Button(main, text="7").grid(column=1, row=3)
ttk.Button(main, text="8").grid(column=2, row=3)
ttk.Button(main, text="9").grid(column=3, row=3)
ttk.Button(main, text="×").grid(column=4, row=3)
ttk.Button(main, text="plch").grid(column=0, row=4)
ttk.Button(main, text="4").grid(column=1, row=4)
ttk.Button(main, text="5").grid(column=2, row=4)
ttk.Button(main, text="6").grid(column=3, row=4)
ttk.Button(main, text="-").grid(column=4, row=4)
ttk.Button(main, text="C").grid(column=0, row=5)
ttk.Button(main, text="1").grid(column=1, row=5)
ttk.Button(main, text="2").grid(column=2, row=5)
ttk.Button(main, text="3").grid(column=3, row=5)
ttk.Button(main, text="+").grid(column=4, row=5, rowspan=2, sticky=(N,S))
ttk.Button(main, text="AC").grid(column=0, row=6)
ttk.Button(main, text="0").grid(column=1, row=6)
ttk.Button(main, text=".").grid(column=2, row=6)
ttk.Button(main, text="=").grid(column=3, row=6)


root.mainloop()