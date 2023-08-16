from tkinter import Button

BUTTONWIDTH = 30
BUTTONHEIGHT = 30

class StandardButton(Button):
    def __init__(self, parentWidget, text=None, image=None):
        super().__init__(parentWidget, text=text, image=image, width=BUTTONWIDTH, height=BUTTONHEIGHT, compound="c")