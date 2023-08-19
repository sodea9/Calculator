#TODO: comma handling
#      floating point
#      overflows
#      leading 0s
#      always display 0

def num_button(toAppend, textVar):
    toAppend = str(toAppend)
    currentText = textVar.get()
    textVar.set(currentText + toAppend)

def backspace(textVar):
    currentText = textVar.get()
    textVar.set(currentText[:len(currentText)-1])

def all_clear():
    pass

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