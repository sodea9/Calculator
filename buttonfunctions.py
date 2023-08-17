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