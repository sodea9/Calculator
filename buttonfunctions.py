#TODO: comma handling
#      floating point
#      overflows
#      leading 0s
#      always display 0
#      = button repeat operator functionality

def comma_parse(number):
    #add commas every 3rd number
    pass

def num_button(toAppend, textVar):
    toAppend = str(toAppend)
    currentValue = textVar.get()
    if currentValue == "0":
        textVar.set(toAppend)
    else:
        textVar.set(currentValue + toAppend)

def backspace(textVar):
    currentValue = textVar.get()
    if len(currentValue)==1:
        textVar.set("0")
    else:
        textVar.set(currentValue[:len(currentValue)-1])

def temp_clear(textVar):
    textVar.set("0")

def all_clear(textVar, memory):
    textVar.set("0")
    memory.set(0)

def add(textVar):
    pass

def subtract(textVar):
    pass

def multiply(textVar):
    pass

def divide(textVar):
    pass

def equals(textVar):
    #save operator function in variable then pass it to this function to execute
    pass

def decimal(textVar):
    pass

def reciprocal(textVar):
    pass

def square(textVar):
    pass

def square_root(textVar):
    pass

def percent(textVar):
    pass

def plus_minus(textVar):
    pass

def mem_clear(memValue):
    memValue.set(0)

def mem_recall(textVar, memory):
    memValue = memory.get()
    textVar.set(str(memValue))

def mem_add(textVar, memory):
    memValue = memory.get()
    memValue += int(textVar.get())
    memory.set(memValue)

def mem_subtract(textVar, memory):
    memValue = memory.get()
    memValue -= int(textVar.get())
    memory.set(memValue)