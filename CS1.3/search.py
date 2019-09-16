#!python
import math

def linear_search(array, item):
    """return the first index of item in array or None if item is not found"""
    # implement linear_search_iterative and linear_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return linear_search_recursive(array, item)
    return linear_search_recursive(array, item)


def linear_search_iterative(array, item):
    # loop over all array values until item is found
    for index, value in enumerate(array):
        if item == value:
            return index  # found
    return None  # not found


def linear_search_recursive(array, item, index=0):
    if index > len(array) - 1:
        return None
    elif array[index] == item:
        return index
    else:
        return linear_search_recursive(array, item, index + 1)

def binary_search(array, item):
    """return the index of item in sorted array or None if item is not found"""
    # implement binary_search_iterative and binary_search_recursive below, then
    # change this to call your implementation to verify it passes all tests
    #return binary_search_iterative(array, item)
    return binary_search_recursive(array, item)


def binary_search_iterative(array, item):
    max = len(array)-1
    min = 0
    while min <= max:
        middle_index = (min + max) // 2
        middle_item = array[middle_index]
        if item == middle_item:
            return middle_index
        elif item > middle_item:
            min = middle_index + 1
        else:
            max = middle_index - 1
    return None

def binary_search_recursive(array, item, left=None, right=None):
    if left == None:
        left = 0
    if right == None:
        right = len(array) - 1
    middle_index = (left + right) // 2
    middle_item = array[middle_index]
    if left <= right:
        if item == middle_item:
            return middle_index
        elif item > middle_item:
            return binary_search_recursive(array, item, middle_index +1, right )
        elif item < middle_item:
            return binary_search_recursive(array, item, left, middle_index -1 )
    else:
        return None
