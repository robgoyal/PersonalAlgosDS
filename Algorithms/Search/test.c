/* Name: test.c
   Author: Robin Goyal
   Last-Modified: June 19, 2017
   Purpose: Test the linear search algorithm
*/

#include <stdio.h>
#include "linear.c"

/* Test basic functionality of linear search file */
int main(void) {

    int arr[] = {1, 5, 15, 2, 7, 9, 10};
    int index = linear(8, arr, sizeof(arr)/sizeof(arr[0]));

    // Check for non-negative return values (valid index)
    if (index >= 0) {
        printf("The element is at location: %i\n", index);  
    }
}