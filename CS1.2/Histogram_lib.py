import sys
import re, string, timeit, collections
from string import punctuation
import enchant

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)

def get_words(source_text):
    word_list = []
    source = open(source_text,"r")
    new_source = open("Histo.txt","w+")
    checker = enchant.Dict("en_US")
    for lines in source:
        line = lines.split()
        for words in line:
            words.strip()
            word = strip_punctuation(words).lower()
            if word and checker.check(word):
                word_list.append(word)
    finish = collections.Counter(word_list)

    new_source.write("{}".format(finish))

    print("Done")

if __name__ == "__main__":
    params = sys.argv[1:]
    source = str(params[0])

    get_words(source)
