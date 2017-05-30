/* Name: test.c
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Test the stack data structure
*/

#include <assert.h>
#include <stdio.h>
#include "stack.h"
#include "stack.c"

// Test client
int main() {

    // Create empty stack 
    node* test = create();

    /* Insert elements into stack
       Stack elements should be 10, 9, 8, 7, 6 */
    for (int i = 6; i < 11; i++) {
        push(&test, i);
    }

    // Simple test cases
    assert(pop(&test) == 10);
    assert(top(&test) == 9);
    assert(pop(&test) == 9);

    // Free all memory
    destroy(&test);
}
