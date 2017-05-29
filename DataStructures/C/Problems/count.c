/* Name: count.c
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Count the number of occurrences of an int
            in the linked list
*/

#include <stdio.h>
#include <assert.h>
#include "linkedlist.h"
#include "linkedlist.c"

// Prototype function declaration
int countN(node* head, int val);

// Test client
int main() {

    // Create empty linked list
    node* test = create();

    // Insert elements
    insert(&test, 5);
    insert(&test, 5);
    insert(&test, 6);
    insert(&test, 4);

    // Test if correct values returned
    printf("Number of fives is %i\n", countN(test, 5));
    printf("Number of sixes is %i\n", countN(test, 6));
    printf("Number of threes is %i\n", countN(test, 3));

    // Destroy list
    destroy(&test);
}

// Return the number of occurrences of an int
int countN(node* head, int val) {

    // Set traversal pointer to head
    node* current = head;

    int count = 0;

    // Iterate through linked list
    while (current != NULL) {

        // Increment count if node value is equal to val
        if (current -> data == val) {
            count++;
        }

        current = current -> next;
    }

    return count;
}