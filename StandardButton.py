from tkinter import Button

BUTTONWIDTH = 60
BUTTONHEIGHT = 60

class StandardButton(Button):
    def __init__(self, parentWidget, text=None, image=None):
        super().__init__(parentWidget, text=text, image=image, width=BUTTONWIDTH, height=BUTTONHEIGHT, compound="c")