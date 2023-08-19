#TODO: comma handling
#      floating point
#      overflows
#      leading 0s
#      always display 0
#      = button repeat operator functionality

def num_button(toAppend, textVar):
    toAppend = str(toAppend)
    currentValue = textVar.get()
    textVar.set(currentValue + toAppend)

def backspace(textVar):
    currentValue = textVar.get()
    textVar.set(currentValue[:len(currentText)-1])

def temp_clear(textVar):
    textVar.set("0")


def all_clear(textVar, memValue):
    textVar.set("0")
    memValue = 0

def add():
    pass

def subtract():
    pass

def multiply():
    pass

def divide():
    pass

def equals():
    pass

def decimal():
    pass

def reciprocal():
    pass

def square():
    pass

def root():
    pass

def percent():
    pass

def plus_minus():
    pass

def mem_clear():
    pass

def mem_recall():
    pass

def mem_add():
    pass

def mem_subtract():
    pass