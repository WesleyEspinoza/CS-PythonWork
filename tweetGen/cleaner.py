from string import punctuation
import math
import re

def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


def clean():
    text = open("original_text.txt", 'r')
    clean_text = ""

    new_text = open("clean_text.txt", 'w+')
    regex = re.compile('[^a-zA-Z]')

    for lines in text:
        line = lines.split()

        for words in line:
            
            words.strip()
            word = regex.sub('', words)
            clean_text = "{} {}".format(clean_text, word)

    new_text.write(clean_text)

    new_text.close()
clean()
