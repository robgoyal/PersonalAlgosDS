# Name: selectionSort.py
# Author: Robin Goyal
# Last-Modified: January 31, 2018
# Purpose: Implement the Selection Sort algorithm


def selection_sort(L):
    '''
    (list: int) -> list

    Returns a sorted list of integers using selection sort.

    >>> selection_sort([5, 2, 1, 3, 6, 4, 9, 7, 8])
    [1, 2, 3, 4, 5, 6, 7, 8, 9]
    '''

    data = list(L)

    for i in range(len(data)):

        # Index for minimum value in data[i:]
        min_index = i
        for j in range(i, len(data)):
            if data[j] < data[min_index]:
                min_index = j

        if i != min_index:
            data[i], data[min_index] = data[min_index], data[i]

    return data
