import sys
import re, string, timeit, random
from string import punctuation


def strip_punctuation(s):
    return ''.join(c for c in s if c not in punctuation)


def get_words():
    word_dict = {}
    accumulator = 0
    words = "one fish two fish red fish blue fish".split(' ')
    for word in words:
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

    rand_sum = random.randint(1,sum(word_dict.values()))

    for key, value in word_dict.items():
        accumulator += value
        if accumulator >= rand_sum:
            return key
        else:
            continue

if __name__ == "__main__":
    print(get_words())
