import sys
import re, string, timeit
from string import punctuation
import enchant

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def get_words(source_text):
    file = open(source_text, "r")
    checker = enchant.Dict("en_US")
    word_dict = {}
    for lines in file:
        line = lines.split()
        for words in line:
            words.strip()
            word = strip_punctuation(words).lower()
            if word and checker.check(word):
                if word in word_dict:
                    word_dict[word] += 1
                else:
                    word_dict[word] = 1

    print(word_dict)

if __name__ == "__main__":
    params = sys.argv[1:]
    source = str(params[0])

    get_words(source)
