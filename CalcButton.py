from tkinter import Button

class CalcButton(Button):
    def __init__(self, masterWidget, text=None, image=None):
        super().__init__(masterWidget, text=text, image=image, width=8, height=5)