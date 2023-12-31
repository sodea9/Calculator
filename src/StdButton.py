from tkinter.ttk import Button

BUTTONWIDTH = 3
PADDING = 8

class StdButton(Button):
    def __init__(self, parentWidget, command=None, text=None, image=None):
        super().__init__(parentWidget, text=text, image=image, padding=PADDING, width=BUTTONWIDTH, command=command)