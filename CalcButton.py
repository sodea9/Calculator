from tkinter.ttk import Button

class CalcButton(Button):
    def __init__(self, masterWidget, text=None, image=None):
        Button(masterWidget, text=text, image=image)
        # self.width = 100
        # self.height = 100
        # self.master = masterWidget
        # self.text = text
        # self.image = image
