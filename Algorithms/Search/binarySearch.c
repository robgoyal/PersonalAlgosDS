/* Name: binarySearch.c
   Author: Robin Goyal
   Last-Modified: June 20, 2017
   Purpose: Perform the binary search operation on array which is O(logn)
            algorithm whose main caveat is that the array must be sorted.
            This a recursive implementation to the binary search. 
*/

#include <stdio.h>
#include <stdbool.h>

// Protoype declaration
bool binarySearch(int value, int values[], int lo, int hi);

int main(void) {

    int arr[] = {1, 2, 5, 6, 10, 15, 22, 27, 39, 46, 65};

    // Check if element exists in array
    if (binarySearch(50, arr, 0, sizeof(arr)/sizeof(arr[0]))) {
        printf("Element exists in array!\n");
    }
    else {
        printf("Element doesn't exist in array!\n");
    }
}

// Recursive binary search algorithm
bool binarySearch(int value, int values[], int lo, int hi) {

    int mid = (hi + lo)/2;

    if (hi <= lo) {
        return false;
    }

    // Look through left side
    else if (value < values[mid]) {
        return binarySearch(value, values, lo, mid - 1);
    }

    // Look through right side
    else if (value > values[mid]) {
        return binarySearch(value, values, mid + 1, hi);
    }

    // Element must exist
    else {
        return true;
    }
}