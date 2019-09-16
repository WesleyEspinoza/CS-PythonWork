#!python
import time

def contains(text, pattern):
    start = time.time()
    """Return a boolean indicating whether pattern occurs in text."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # calls find_all_indexes passing in the text, pattern, True (because we want True or False), False (because we do not want the first index), False (because we do not want all indexes)
    stop = time.time()
    print('Time to complete function: {}'.format(stop-start))
    return find_all_indexes(text,pattern,0)



def find_index(text, pattern):
    """Return the starting index of the first occurrence of pattern in text,
    or None if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # calls find_all_indexes passing in the text, pattern, False (because we do not want True or False), True (because we want the first index), False (because we do not want all indexes)
    return find_all_indexes(text,pattern,1)


def find_all_indexes(text, pattern,returning=2):
    start = time.time()
    """Return a list of starting indexes of all occurrences of pattern in text,
    or an empty list if not found."""
    assert isinstance(text, str), 'text is not a string: {}'.format(text)
    assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)
    # TODO: Implement find_all_indexes here (iteratively and/or recursively)
    # init basic varaibles that will be needed.
    answer = []
    text_length = len(text) - 1


    #check if patter given is empty
    if pattern == '':
        #check for what return is wanted.
        if returning == 0:
            print('True')
            stop = time.time()
            print('Time to complete function: {}'.format(stop-start))
            return True
        #check for what return is wanted.
        elif returning == 1:
            print('0')
            stop = time.time()
            print('Time to complete function: {}'.format(stop-start))
            return 0
        #if neither are checked off use default
        else:
            for i in range(text_length +1):
                answer.append(i)
            print(answer)
            stop = time.time()
            print('Time to complete function: {}'.format(stop-start))
            return answer


        #more variables to init
    pattern_start = pattern[0]
    current_pattern = ''
    pattern_length = len(pattern) - 1
    current_pattern_length = 0
    index = 0


        # iterate through all the letters in te given text.
    for letter in text:
        #check if letter is equal to the start of the patter given.
        if letter == pattern_start:
        #while the current patter is not the same length appened a letter until it is.
            while current_pattern_length <= pattern_length and index <= text_length and current_pattern_length+index <= text_length:
                current_pattern += text[index+current_pattern_length]
                current_pattern_length += 1


            #Check current patter against the given pattern
            if current_pattern == pattern:
                #if the same appened the index of where it was found
                answer.append(index)
                #reset the pattern and the legnth of the pattern
                current_pattern = ''
                current_pattern_length = 0
            else:
                #if not the same reset because it is not what we need.
                current_pattern = ''
                current_pattern_length = 0


        index += 1

        # once the index has gone past the text legnth it's time to make a return
        if index > text_length:
            #check for what return is wanted.
            if returning == 0:
                # if the legnth of answer is less then 0 return False because nothing was found
                if len(answer) - 1 < 0:
                    print('False')
                    stop = time.time()
                    print('Time to complete function: {}'.format(stop-start))
                    return False
                else:
                    print('True')
                    stop = time.time()
                    print('Time to complete function: {}'.format(stop-start))
                    return True


            #check for what return is wanted.
            if returning == 1:
                if len(answer) - 1 < 0:
                    print(None)
                    stop = time.time()
                    print('Time to complete function: {}'.format(stop-start))
                    return None
                else:
                    print(answer[0])
                    stop = time.time()
                    print('Time to complete function: {}'.format(stop-start))
                    return answer[0]

            #check for what return is wanted.
            if returning > 1:
                print(answer)
                stop = time.time()
                print('Time to complete function: {}'.format(stop-start))
                return answer


def test_string_algorithms(text, pattern):
    found = contains(text, pattern)
    print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
    # TODO: Uncomment these lines after you implement find_index
    index = find_index(text, pattern)
    print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
    # TODO: Uncomment these lines after you implement find_all_indexes
    indexes = find_all_indexes(text, pattern)
    print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
    """Read command-line arguments and test string searching algorithms."""
    import sys
    args = sys.argv[1:]  # Ignore script file name
    if len(args) == 2:
        text = args[0]
        pattern = args[1]
        test_string_algorithms(text, pattern)
    else:
        script = sys.argv[0]
        print('Usage: {} text pattern'.format(script))
        print('Searches for occurrences of pattern in text')
        print("\nExample: {} 'abra cadabra' 'abra'".format(script))
        print("contains('abra cadabra', 'abra') => True")
        print("find_index('abra cadabra', 'abra') => 0")
        print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
    main()
