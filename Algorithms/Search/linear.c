/* Name: linear.c
   Author: Robin Goyal
   Last-Modified: June 19, 2017
   Purpose: Returns the index of element in array by linear search
            O(n) operation on any array orientation (sorted vs unsorted)
*/

#include <stdio.h>

/* Function returns -1 or -2 for errors not associated with index of
   array. Test file checks for a return value greater than 0 for a
   valid index. Length must be passed as parameter since array passed
   as parameter to a function is a pointer for which len of pointer doesnt
   return actual length of array. */

int linear(int value, int values[], int len) {

    // Check for nonempty array
    if (len == 0) {
        printf("Empty array\n");
        return -2;
    }

    // Linearly search for element
    for (int i = 0; i < len; i++) {
        if (value == values[i]) {
            return i;
        }
    }

    printf("Element not in array\n");
    return -1;
}

