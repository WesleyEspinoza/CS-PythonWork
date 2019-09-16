'''Given a sorted list and an input number as inputs,
 write a function to return a Range object, consisting of
 the indices of the first and last occurrences of the
 input number in the list. Check out the Use Me section to
 examine the structure of the Range class.'''

def find_range(input_list,input_number):
    first = input_list.index(input_number)
    last = len(input_list) - input_list[::-1].index(input_number) - 1
    print[first, last]
    return [first, last]
