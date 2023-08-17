#TODO: Styling
#      Resizing
#      Theme option in settings
#      breeze-dark, awdark

import tkinter as tk
from tkinter import ttk, font, Frame, Button, Entry, N, W, E, S
from ttkthemes import ThemedTk
import sv_ttk
import customtkinter
from StdButton import *

root = tk.Tk()
#root = ThemedTk()
#root = customtkinter.CTk()
root.title("Calculator")
icon = tk.PhotoImage(file="calcicon.png")
root.iconphoto(False, icon)

main = Frame(root, padx=3, pady=3)
main.grid(column=0, row=0, sticky=(N,W,E,S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

root.tk.call("lappend", "auto_path", "TkCustomThemes/awthemes-10.4.0")
root.tk.call("package", "require", "awdark")
s = ttk.Style(root)
s.theme_use("vista")
#print(root.get_themes())
print(s.theme_names())
#sv_ttk.set_theme("dark")
#customtkinter.set_appearance_mode("System")
#customtkinter.set_default_color_theme("blue")

defaultFont = font.nametofont("TkDefaultFont")
defaultFont.configure(family="Helvetica", size=20)

numEntry = Entry(main, width=1, justify="right", font=("Helvetica 35"))
numEntry.grid(column=0, row=0, sticky=(N, W, E), columnspan=5)

StdButton(main, text="plch").grid(column=1, row=1)
StdButton(main, text="plch").grid(column=2, row=1)
StdButton(main, text="plch").grid(column=3, row=1)
StdButton(main, text="⌫").grid(column=4, row=1)
StdButton(main, text="MC").grid(column=0, row=2)
StdButton(main, text="MR").grid(column=1, row=2)
StdButton(main, text="M−").grid(column=2, row=2)
StdButton(main, text="M+").grid(column=3, row=2)
StdButton(main, text="÷").grid(column=4, row=2)
StdButton(main, text="%").grid(column=0, row=3)
StdButton(main, text="7").grid(column=1, row=3)
StdButton(main, text="8").grid(column=2, row=3)
StdButton(main, text="9").grid(column=3, row=3)
StdButton(main, text="×").grid(column=4, row=3)
StdButton(main, text="plch").grid(column=0, row=4)
StdButton(main, text="4").grid(column=1, row=4)
StdButton(main, text="5").grid(column=2, row=4)
StdButton(main, text="6").grid(column=3, row=4)
StdButton(main, text="−").grid(column=4, row=4)
StdButton(main, text="C").grid(column=0, row=5)
StdButton(main, text="1").grid(column=1, row=5)
StdButton(main, text="2").grid(column=2, row=5)
StdButton(main, text="3").grid(column=3, row=5)
StdButton(main, text="+").grid(column=4, row=5, rowspan=2, sticky=(N,S))
StdButton(main, text="AC").grid(column=0, row=6)
StdButton(main, text="0").grid(column=1, row=6)
StdButton(main, text=".").grid(column=2, row=6)
StdButton(main, text="=").grid(column=3, row=6)

numEntry.focus()
root.mainloop()