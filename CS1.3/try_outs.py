#!python

import string
import math
import re
# Hint: Use these string constants to encode/decode hexadecimal digits and more
# string.digits is '0123456789'
# string.hexdigits is '0123456789abcdefABCDEF'
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase
# string.printable is digits + ascii_letters + punctuation + whitespace


def decode(digits, base):
    """Decode given digits in given base to number in base 10.
    digits: str -- string representation of number (in given base)
    base: int -- base of given number
    return: int -- integer representation of number (in base 10)"""
    answer = 0
    assert 2 <= base <= 36, 'base is out of range: {}'.format(base)
    conversion_values = string.printable
    r_digits = str(digits[::-1].lower())
    for index, given_value in enumerate(r_digits,0):
        converted_value = conversion_values.index(given_value)
        answer += converted_value*(base**index)
    if answer == 0:
        print (0)
    else:
        print (answer)



def encode(number, base):
    """Encode given number in base 10 to digits in given base.
    number: int -- integer representation of number (in base 10)
    base: int -- base to convert to
    return: str -- string representation of number (in given base)"""
    # Handle up to base 36 [0-9a-z]
    assert 2 <= base, 'base is out of range: {}'.format(base)
    # Handle unsigned numbers only for now
    assert number >= 0, 'number is negative: {}'.format(number)
    n = int(number)
    b = int(base)
    answer = []
    conversion_values = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ+/'
    if b == 64:
        conversion_values = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/'
    while n != 0:
        r = n%b
        answer.append(conversion_values[r])
        n = n//b
    print( "".join(answer[::-1]))


def binary_search_iterative(array, item):
    # TODO: implement binary search iteratively here
    array_length = len(array) - 1
    middle_index = array_length//2
    max = array_length
    min = 0
    nothing = False
    if array[0] == item:
        return 0
    elif array[1] == item:
        return 1
    elif array[array_length] == item:
        return array_length
    elif array[array_length-1] == item:
        return array_length - 1
    else:
        while array[middle_index] != item and nothing == False:
            if item > array[middle_index]:
                temp_mid_index = math.ceil((min + max) // 2)
                min = temp_mid_index
                middle_index = temp_mid_index
            elif item < array[middle_index]:
                temp_mid_index = math.ceil((max)/ 2)
                max = temp_mid_index
                middle_index = temp_mid_index
            if min+max == 1 or min+max == array_length + array_length - 1:
                nothing = True
                return None

        return middle_index

def is_palindrome_iterative(text):
    clean_text = re.sub('[^A-Za-z0-9]+', '', text)
    reversed_text = ''
    text_length = len(text) - 1
    current_index = text_length
    while current_index >= 0:
        reversed_text += clean_text[current_index]
        current_index -= 1
    if str.lower(reversed_text) == str.lower(clean_text):
        print('R: {}, T: {}'.format(reversed_text, clean_text))
        print('True')
    else:
        print('R: {}, T: {}'.format(reversed_text, clean_text))
        print('False')

def is_palindrome_recursive(text, current_index=0, reversed_word=''):
    clean_text = re.sub('[^A-Za-z0-9]+', '', text.lower())
    text_length = len(clean_text)-1
    if current_index > text_length:
        if reversed_word == clean_text:
            print('True')
        else:
            print("False")
    print('Text Length: {}, current_index: {}'.format(text_length,current_index))
    return is_palindrome_recursive(text, current_index + 1, reversed_word + clean_text[text_length - current_index])

def contains(text, pattern):
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    if pattern == '' or None:
        print('True')
        return True
    pattern_start = pattern[0]
    current_pattern = ''
    current_index = 0
    pattern_length = len(pattern) - 1
    text_length = len(text) - 1
    current_pattern_length = 0
    index = 0

    for letter in text:
        if letter == pattern_start:
            while current_pattern_length <= pattern_length and index <= text_length:
                current_pattern += text[index+current_pattern_length]
                current_pattern_length += 1
            if current_pattern == pattern:
                print('True')
                print('pattern: {}, Current_pattern: {}, Text: {}, Index: {}'.format(pattern, current_pattern, text, index))
                return True
            else:
                current_pattern = ''
                current_pattern_length = 0
        index += 1
        if index > len(text) -1:
            print('False')
            print('pattern: {}, Current_pattern: {}, Text: {}, Index: {}, text_length: {}'.format(pattern, current_pattern, text, index, text_length))
            return False






# contains('abc', '')
# contains('abc', 'a')
# contains('abc', 'b')
contains('abc', 'c')
# contains('abc', 'ab')
# contains('abc', 'bc')
# contains('abc', 'abc')
# contains('aaa', 'a')
# contains('aaa', 'aa')
# contains('ababc', 'ab')
# contains('banana', 'na')
# contains('ababc', 'abc')
# contains('bananas', 'nas')
