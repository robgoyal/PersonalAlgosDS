/* Name: getNth.c
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Returns the nth index of the linked list
*/

#include <assert.h>
#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"
#include "linkedlist.c"

// Prototype declaration
int GetNth(node* head, int index);

// Test client
int main() {

    // Create empty linked list
    node* test = create();
        
    /* Insert elements into linked list
       List after loop should be 5 -> 4 -> 3 -> 2 -> 1 -> 0
    */
    for (int i = 0; i < 6; i++) {
        insert(&test, i);
    }

    // Simple tests for first and last index
    assert(GetNth(test, 0) == 5);
    assert(GetNth(test, 5) == 0);

    // Free memory in heap
    destroy(&test);

}

// Return the value at index of list
int GetNth(node* head, int index) {

    // Check if index falls between (0, length -1)
    if (index < 0 || index > length(&head) - 1) {
        printf("Index out of bounds.\n");

        // Free allocated memory and exit
        destroy(&head);
        exit(1);
    }

    // Create traversal pointer
    node* current = head;

    // Traverse through list until index count reaches 0
    while (index > 0) {
        current = current -> next;
        index--;
    }

    return current -> data;
}