# Name: insertionSort.py
# Author: Robin Goyal
# Last-Modified: January 30, 2018
# Purpose: Implement the Insertion Sort algorithm


def insertion_sort(L):
    '''
    (list: int) -> list

    Returns a sorted list of integers in ascending order.

    >>> insertion_sort([5, 2, 4, 6, 1, 3])
    [1, 2, 3, 4, 5, 6]
    '''

    # Create copy of data
    data = list(L)

    # First element is always sorted
    for i in range(1, len(data)):

        sorted_index = i

        # At most i swaps are required
        for j in range(i):

            # Perform swap
            if data[sorted_index] < data[sorted_index - 1]:
                data[sorted_index], data[sorted_index - 1] = data[sorted_index - 1], data[sorted_index]
                sorted_index -= 1

    return data
