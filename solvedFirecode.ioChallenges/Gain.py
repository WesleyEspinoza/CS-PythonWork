
'''Given an list of integers,
write a method - max_gain - that returns the maximum gain.
Maximum Gain is defined as the maximum difference between 2 elements
in a list such that the larger element appears
 after the smaller element. If no gain is possible, return 0.'''

def max_gain(input_list):
    if len(input_list) < 2:
        return 0
    a = input_list[0]
    max_val = 0
    for i in input_list[1:]:
        max_val = max(max_val, i-a)
        a = min(a, i)
    return max_val
