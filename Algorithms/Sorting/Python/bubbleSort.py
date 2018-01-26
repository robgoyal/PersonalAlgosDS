# Name: bubbleSort.py
# Author: Robin Goyal
# Last-Modified: January 26, 2018
# Purpose: Implement the bubble sort algorithm


def bubble_sort(data):
    '''
    (list: int) -> list:int

    Returns a copy of the list with the integers in data sorted
    in ascending order using the bubble sort algorithm.

    >>> bubble_sort([3, 2, 1])
    [1, 2, 3]
    >>> bubble_sort([2, 1, 7, 9, 10, 5, 6, 11])
    [1, 2, 5, 6, 7, 9, 10, 11]
    '''

    # Copy data from original list
    copy_data = list(data)

    # Initialize swaps to enter while condition
    swaps = True

    # Loop until no swaps have occurred
    while swaps:

        # Exits from while if no swaps occur
        swaps = False

        for i in range(len(copy_data) - 1):

            # Swap elements if out of place
            if copy_data[i] > copy_data[i + 1]:
                copy_data[i + 1], copy_data[i] = copy_data[i], copy_data[i + 1]
                swaps = True

    return copy_data
