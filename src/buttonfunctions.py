#TODO:
#      error messages
#      function edge cases
#      return to int if it returns to a cardinal number
#      overflows
#      = button repeat operator functionality
#double check negatives work after adding minus button
#      **main operators
#      **floating point support

from math import sqrt

def add_commas(number:int) -> str:
    return f'{number:,}'

def comma_parse_recursive(number:str) -> str:
    # Didn't end up needing this but I'm going to leave it here because I'm proud of it :)
    if len(number) <= 3:
        return number
    else:
        slice = number[-3:]
        remainder = comma_parse_recursive(number[:-3])
    return ",".join([remainder, slice])

def remove_commas(number:str) -> int:
    return number.replace(",", "")

def reformat(number) -> str:
    if not isinstance(number, str):
        raise ValueError("How many times do we have to teach you this lesson old man?")
    
    number = remove_commas(number)
    return add_commas(int(number))

def get_raw_number(textVar):
    commaNum = textVar.get()
    return int(remove_commas(commaNum))

def num_button(toAppend, textVar, operator):
    if operator:
        textVar.set("0")
    toAppend = str(toAppend)
    currentValue = textVar.get()
    if currentValue == "0":
        textVar.set(toAppend)
    else:
        toDisplay = currentValue + toAppend
        formatted = reformat(toDisplay)
        textVar.set(formatted)

def backspace(textVar):
    currentValue = textVar.get()
    if len(currentValue)==1:
        textVar.set("0")
    else:
        toDisplay = currentValue[:len(currentValue)-1]
        formatted = reformat(toDisplay)
        textVar.set(formatted)

def temp_clear(textVar):
    textVar.set("0")

def all_clear(textVar, memory):
    textVar.set("0")
    memory.set(0)

def add(textVar, saved) -> str:
    saved.set(saved.get() + get_raw_number(textVar))
    return "+"

def subtract(textVar, saved) -> str:
    saved.set(saved.get() - get_raw_number(textVar))
    return "-"

def multiply(textVar, saved) -> str:
    saved.set(saved.get() * get_raw_number(textVar))
    return "*"

def divide(textVar, saved) -> str:
    saved.set(saved.get() / get_raw_number(textVar))
    return "/"

def equals(textVar, saved, operator):
    if operator == "+":
        textVar.set(add_commas(saved.get() + get_raw_number(textVar)))
    if operator == "-":
        textVar.set(add_commas(saved.get() - get_raw_number(textVar)))
    if operator == "*":
        textVar.set(add_commas(saved.get() * get_raw_number(textVar)))
    if operator == "/":
        textVar.set(add_commas(saved.get() / get_raw_number(textVar)))

def decimal(textVar):
    pass

def reciprocal(textVar):
    currentValue = get_raw_number(textVar)
    if currentValue == 0:
        textVar.set("Error")
    textVar.set(add_commas(1 / currentValue))

def square(textVar):
    currentValue = get_raw_number(textVar)
    textVar.set(add_commas(currentValue ** 2))

def square_root(textVar):
    currentValue = get_raw_number(textVar)
    textVar.set(add_commas(sqrt(currentValue)))

def percent(textVar):
    currentValue = get_raw_number(textVar)
    textVar.set(add_commas(currentValue / 100))

def plus_minus(textVar):
    currentValue = get_raw_number(textVar)
    if currentValue < 0:
        return
    textVar.set(add_commas(currentValue * -1))

def mem_clear(memValue):
    memValue.set(0)

def mem_recall(textVar, memory):
    memValue = memory.get()
    textVar.set(add_commas(memValue))

def mem_add(textVar, memory):
    memValue = memory.get()
    memValue += get_raw_number(textVar)
    memory.set(memValue)

def mem_subtract(textVar, memory):
    memValue = memory.get()
    memValue -= get_raw_number(textVar)
    memory.set(memValue)