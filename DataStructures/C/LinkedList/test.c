/* Name: test.c
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Basic test file for linked list data structure
*/

#include <stdio.h>
#include <assert.h>
#include "linkedlist.h"
#include "linkedlist.c"

int main() {

    // Create empty linked list
    node* test = create();

    // Test for empty linked list
    assert(test == NULL);
    
    /* Insert elements into list
    List should be 9 -> 8 -> 7 -> 6 -> 5 */
    for (int i = 0; i < 5; i++) {
        insert(&test, i + 5); 
    }

    // No error thrown
    assert(find(&test, 6));

    // Throws error since list doesn't include 1
    assert(find(&test, 1));

    // Destroy list
    destroy(&test);
}