"""
Notes:
Widgets
    -Buttons
    -Labels
    -Frames
    -Entries
    -Checkboxes
    -Tree Views
    -Scroll bars
    -Text Areas
    Widgets won't be garbage collected even if they don't have a saved reference

Text variables
    Use type StringVar
    can attach entry boxes to them or text labels
    if the entry box changes, the attached variable will automatically update
    if the variable is updated, the label widget will automatically update
"""

import tkinter as tk
from tkinter import ttk, N, W, E, S

#Performing the calculation
def calculate(*args):
    try:
        value = float(feet.get())
        meters.set(int(0.3048 * value * 10000.0 + 0.5)/10000.0)
    except ValueError:
        pass
    

#Setting up the main application window
root = tk.Tk() #always included
root.title("Feet to Meters") #titles window

#Creating a content frame
mainframe = ttk.Frame(root, padding="3 3 12 12") #creates frame widget
mainframe.grid(column=0, row=0, sticky=(N,W,E,S)) #places directly in main window
root.columnconfigure(0, weight=1) #resizes to fill extra space
root.rowconfigure(0, weight=1) #resizes to fill extra space

#Creating the entry widget
feet = tk.StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet) #parent widget is mainframe, 7 characters wide
feet_entry.grid(column=2, row=1, sticky=(W,E)) #places at appropriate place in layout grid, sticky determines which sides of the cell the widget is anchored to

#Creating the remaining widgets
meters = tk.StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W,E))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

#Adding some polish
for child in mainframe.winfo_children(): #adds padding to each of the widgets
    child.grid_configure(padx=5, pady=5)
feet_entry.focus() #automatically moves cursor to entry box
root.bind("<Return>", calculate) #if enter is pressed it will run the calculate command

#Start the event loop
root.mainloop() #always included (keeps event loop running)