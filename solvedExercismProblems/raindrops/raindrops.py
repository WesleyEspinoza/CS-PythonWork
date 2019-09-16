from math import sqrt
from functools import reduce

def get_factors(number):
        step = 2 if number%2 else 1
        return set(reduce(list.__add__,([i, number//i] for i in range(1, int(sqrt(number))+1, step) if number % i == 0)))
def convert(number):
    result = []
    factors = get_factors(number)
    print(factors)
    for number in factors:
        if number == 3:
            result.append('Pling')
        if number == 5:
            result.append('Plang')
        if number == 7:
            result.append('Plong')

    if len(result) == 0:
        return ''.format(number)
    else:
        return result


print(8)
