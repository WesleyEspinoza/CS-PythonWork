import sys
import re, string, timeit, collections
from string import punctuation
import enchant

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

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
                for i in range(0,len(word_list)):
                    current_tup = word_list[i]
                    if word == current_tup[0]:
                        track = current_tup[1] + 1
                        new_tup = (current_tup[0], track)
                        word_list[i] = new_tup
                else:
                    temp_list = (word, 1)
                    word_list.append(temp_list)

    print(word_list)


if __name__ == "__main__":
    params = sys.argv[1:]
    source = str(params[0])

    get_words(source)
