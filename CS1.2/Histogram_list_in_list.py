import sys
import re, string, timeit, collections
from string import punctuation
import enchant

def strip_punctuation(string):
    return ''.join(c for c in string if c not in punctuation)

def get_words(source_text):
    file = open(source_text, "r")
    checker = enchant.Dict("en_US")
    word_list = list()
    for lines in file:
        line = lines.split()
        for words in line:
            words.strip()
            word = strip_punctuation(words).lower()
            if word and checker.check(word):
                for items in word_list:
                    if word == items[0]:
                        items[1] += 1
                else:
                    temp_list = list()
                    temp_list.append(word)
                    temp_list.append(1)
                    word_list.append(temp_list)

    print(word_list)


if __name__ == "__main__":
    params = sys.argv[1:]
    source = str(params[0])

    get_words(source)
