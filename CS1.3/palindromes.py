#!python

import string
import re
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
    """A string of characters is a palindrome if it reads the same forwards and
    backwards, ignoring punctuation, whitespace, and letter casing."""
    # implement is_palindrome_iterative and is_palindrome_recursive below, then
    # change this to call your implementation to verify it passes all tests
    assert isinstance(text, str), 'input is not a string: {}'.format(text)
    #return is_palindrome_iterative(text)
    return is_palindrome_recursive(text)


def is_palindrome_iterative(text):
    # clean_text = re.sub('[^A-Za-z0-9]+', '', text.lower())
    # reversed_text = ''
    # text_length = len(clean_text) - 1
    # current_index = text_length
    # while current_index >= 0:
    #     reversed_text += clean_text[current_index]
    #     current_index -= 1
    # if reversed_text == clean_text:
    #     return True
    # else:
    #     return False
    clean_text = re.sub('[^A-Za-z0-9]+', '', text.lower())
    return clean_text == clean_text[::-1]


def is_palindrome_recursive(text, current_index=0, reversed_word=''):
    clean_text = re.sub('[^A-Za-z0-9]+', '', text.lower())
    text_length = len(clean_text)-1
    if current_index > text_length:
        if reversed_word == clean_text:
            return True
        else:
            return False
    return is_palindrome_recursive(text, current_index + 1, reversed_word + clean_text[text_length - current_index])

def main():
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) > 0:
        for arg in args:
            is_pal = is_palindrome(arg)
            result = 'PASS' if is_pal else 'FAIL'
            is_str = 'is' if is_pal else 'is not'
            print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
    else:
        print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
        print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
    main()
