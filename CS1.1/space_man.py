
'''
Variables should be more specific


'''

import random
from nltk.corpus import words
import os
clear = lambda: os.system('clear')
word_list = words.words()
secret_word = ""
secret = []
guessed_letters = []
guesses = 0
won = 0
def user_input(prompt):

    # the input function will display a message in the terminal
    # and wait for user input.
    user_input = input(prompt)
    return user_input

def ranword():
    global secret_word
    secret_word = random.choice(word_list)
    secret_word.lower()

def update(index, item):
    secret[index] = item

ranword()

def print_underscores():
    global word_length
    for i in range(0,len(secret_word)):
        secret.append("_")
    clear()
    print(secret)

print_underscores()

def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

def select(function_code):
    global guesses
    global secret_word
        #create item
    if function_code == "1":
        return False
    elif guesses >= 7:
        clear()
        print("you ran out of tries your spaceman has been sent to space")
        print("the word was " + secret_word)
        return False
    else:
#use str.find to check if athe letter is in the secret word
        if function_code in guessed_letters:
            clear()
            print("letter has already been guessed")
            return True
        else:
            if secret_word.find(selection) != -1:
                for i in find(secret_word,selection):
                    update(i,selection)
                clear()
                print(secret)
                print("Guessed letters ",guessed_letters)
                return True
            else:
                guesses += 1
                guessed_letters.append(function_code)
                clear()
                print(secret)
                print("Guessed letters ",guessed_letters)
            return True
def run():
    try:
        running = True
        while running:
            selection = user_input(" guess a letter or type '1' to quit\n ").lower()
            if len(selection) == 1 and selection.isalpha() or selection == "1":
                running = select(selection.lower())
            else:
                print("you can only type in one alpha character")
    except EOFError:
            print("please stop")
            run()

run()
