
from termcolor import colored
import os
clear = lambda: os.system('clear')
checklist = list()
def create(item):
    checklist.append(item)
    #checklist[0]

def read(index):
    clear()
    print(colored(checklist[index], 'red'))
    return checklist[index]

def update(index, item):
    clear()
    checklist[index] = item

def destroy(index):
    checklist.pop(index)


def list_all_items():
    clear()
    index = 0
    for list_item in checklist:
        print(colored("{} {}".format(index, list_item), 'red'))
        index += 1

def mark_complete(index):
    update(index, "{} {}".format("√", checklist[index]))


def user_input(prompt):

    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    clear()
    return user_input


def select(function_code):
    #create item
    if function_code == "A" or function_code == "a":
        input_item = user_input("item to add: \n")
        create(input_item)
    #readItem
    elif function_code == "R" or function_code == "r":
        try:
            item_index = int(user_input("Index Number?: \n"))
            if item_index > len(checklist)-1:
                print("Input not valid")
            else:
                read(item_index)
        except ValueError:
                    print("That's not an int!")
        #mark Item Complete
    elif function_code == "C" or function_code == "c":
        try:
            item_index = int(user_input("Index Number?:\n"))
            if item_index > len(checklist)-1:
                    print("Input not valid")
            else:
                    mark_complete(item_index)
        except ValueError:
                print("That's not an int!")
#print all items
    elif function_code == "P" or function_code == "p":
        list_all_items()

    elif function_code == "RM" or function_code == "rm" or function_code == "rM" or function_code == "Rm":
        try:
            item_index = int(user_input("Index Number?: \n"))
            if item_index > len(checklist)-1:
                print("Input not valid")
            else:
                destroy(item_index)
        except ValueError:
                print("That's not an int!")
    elif function_code == "Q" or function_code == "q":
            # This is where we want to stop our loop
            return False
    else:
        print("Unknown Option")
    return True
'''
def test():
    create("Purple Sox")
    create("Red Cloak")
    print(read(0))
    print(read(1))
    update(0, "Purple Socks")
    destroy(1)
    print(read(0))
    user_value = user_input("Please Enter a value:")
    print(user_value)
    list_all_items()
    select("A")
    list_all_items()
    select("R")
    list_all_items()class


test()
'''
running = True
while running:
    selection = user_input(
        "\003Press A to add to list, R to Read from list, P to display list, C to check items off, RM to remove from list and Q to quit:\n ")
    running = select(selection)
