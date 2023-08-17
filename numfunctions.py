#TODO: comma handling
#      floating point
#      overflows
#      leading 0s

def num_button(toAppend, textVar):
    toAppend = str(toAppend)
    currentText = textVar.get()
    textVar.set(currentText + toAppend)