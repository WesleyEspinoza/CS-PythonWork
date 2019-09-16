from termcolor import colored
import os
import check
clear = lambda: os.system('clear')
inputs = list()
fc = 0

def create(item):
    inputs.append(item)
    #checklist[0]

def update(index, item):
    clear()
    inputs[index] = item

def destroy(index):
    inputs.pop(index)


def list_all_items():
    clear()
    index = 0
    for list_item in inputs:
        print(colored("{} {}".format(index, list_item), 'red'))
        index += 1

def mark_complete(index):
    update(index, "{} {}".format("√", inputs[index]))


def user_input(prompt):

    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    clear()
    return user_input


def select(function_code):
    #create item
    global fc
    if function_code == "A" or function_code == "a":
        input_item = user_input("type in a name \n")
        update(0,input_item)
        fc += 1
    #readItem
    elif function_code == "S" or function_code == "s":
        input_item = user_input("type in a state: \n")
        input_item.lower
        if input_item.capitalize() in check.cities:
            update(1,input_item)
            fc += 1
        else:
            print("Not a State")
        #mark Item Complete
    elif function_code == "D" or function_code == "d":
        input_item = user_input("type in a animal: \n")
        update(2,input_item)
        fc += 1
#print all items
    elif function_code == "F" or function_code == "f":
        input_item = user_input("type in a car brand: \n")
        update(3,input_item)
        fc += 1

    elif function_code == "RM" or function_code == "rm" or function_code == "rM" or function_code == "Rm":
        list_all_items()
        print(check.cities[0])
    elif function_code == "Q" or function_code == "q":
            # This is where we want to stop our loop
            if fc >=4:
                return False
    else:
        print("Unknown Option or you didn't fill everything out")
    return True


def init():
    create("Name")
    create("City")
    create("Animal")
    create("Car")
init()

def test():
    global fc
    q = lambda: os.system('q')
    update(0,'wes')
    update(1,'indianapolis')
    update(2,'black panther')
    update(3,'massurati')
    fc += 4
    q

running = True
while running:
    selection = user_input("Press A to write in a Name, S to write in state, D to write in an animal, F to write in a car brand, and Q to summit:\n ")
    running = select(selection)
