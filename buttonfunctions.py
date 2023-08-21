#TODO: comma handling
#      floating point support
#      overflows
#      = button repeat operator functionality
#      add negative sign handling with commas

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

def format_number(number: str) -> str:
    number = remove_commas(number)
    return add_commas(int(number))

def num_button(toAppend, textVar):
    toAppend = str(toAppend)
    currentValue = textVar.get()
    if currentValue == "0":
        textVar.set(toAppend)
    else:
        toDisplay = currentValue + toAppend
        formatted = format_number(toDisplay)
        textVar.set(formatted)

def backspace(textVar):
    currentValue = textVar.get()
    if len(currentValue)==1:
        textVar.set("0")
    else:
        toDisplay = currentValue[:len(currentValue)-1]
        formatted = format_number(toDisplay)
        textVar.set(formatted)

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