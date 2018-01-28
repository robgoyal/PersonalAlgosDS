# Name: mergeSort.py
# Author: Robin Goyal
# Last-Modified: January 28, 2018
# Purpose: Implement the algorithm for merge sort


def merge_sort(values):
    '''
    (list: int) -> list:int

    Returns values as a sorted list.

    >>> merge_sort([2, 1])
    [1, 2]
    >>> merge_sort([2, 3, 1])
    [1, 2, 3]
    >>> merge_sort([])
    []
    >>> merge_sort([0, 9, 3, 6, 5, 2, 1, 4, 6])
    [0, 1, 2, 3, 4, 5, 6, 6, 9]
    '''

    # Empty list or single element is sorted
    if len(values) <= 1:
        return values

    # Sort the left and right halves
    mid = len(values) // 2
    left = merge_sort(values[:mid])
    right = merge_sort(values[mid:])

    # Merge the sorted left and sorted right half
    return merge(left, right)


def merge(left, right):
    '''
    (list: int, list: int) -> list: int

    Returns the merging of the sorted left
    list and sorted right list.

    >>> merge([1, 2, 3], [0, 4, 6])
    [0, 1, 2, 3, 4, 6]
    >>> merge([9], [1])
    [1, 9]
    >>> merge([2, 5], [1])
    [1, 2, 5]
    '''

    result = []

    # Initialize pointers to traverse over both lists
    left_ptr, right_ptr = 0, 0

    # Loop until either pointer has reached end
    while left_ptr != len(left) and right_ptr != len(right):
        if left[left_ptr] <= right[right_ptr]:
            result.append(left[left_ptr])
            left_ptr += 1
        else:
            result.append(right[right_ptr])
            right_ptr += 1

    # Post-check for any remaining elements in either list
    if left_ptr != len(left):
        result.extend(left[left_ptr:])
    elif right_ptr != len(right):
        result.extend(right[right_ptr:])

    return result
