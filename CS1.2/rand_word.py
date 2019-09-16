from nltk.corpus import words
import random

# takes in user input
def user_input(prompt):
    user_input = input(prompt)
    return user_input

#gets random word from nltk corpus
def get_random_word(Num_of_words):
    for i in range(0,Num_of_words):
        word_list = words.words()
        word = random.choice(word_list)
        print(word)

    #runs everything
if __name__ == '__main__':
    user = user_input("how many words?: \n")
    get_random_word(int(user))
