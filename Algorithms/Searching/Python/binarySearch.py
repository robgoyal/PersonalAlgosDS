# Name: binarySearch.py
# Author: Robin Goyal
# Last-Modified: January 22, 2018
# Purpose: Implement the binary search algorithm


def binary_search(data, val):
    '''
    (list, int) -> bool

    Precondition: data must be sorted.

    Return True if val is in data, a list of integers.

    >>> binary_search([1, 3, 7, 15], 3)
    True
    >>> binary_search([1, 8, 22, 36], 5)
    False
    '''

    low, high = 0, len(data) - 1

    while high >= low:

        # Calculate the midpoint of the current viewing section
        mid = (high + low) // 2

        # Check if val is in greater half of data[low: high + 1]
        if val > data[mid]:
            low = mid + 1

        # Check if val is in smaller half of data[low: high + 1]
        elif val < data[mid]:
            high = mid - 1

        else:
            return True

    return False
