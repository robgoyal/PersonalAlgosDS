# Name: linearSearch.py
# Author: Robin Goyal
# Last-Modified: January 22, 2018
# Purpose: Implement the linear search algorithm


def linear_search(data, val):
    '''
    (list, value) -> bool: where value is any data type

    Return True if val is in the list, data.

    >>> linear_search([1, 2, 3, 4], 3)
    True
    >>> linear_search([True, False, 5, 4], 3)
    False
    '''

    for item in data:
        if item == val:
            return True

    return False
