/* Name: pop.c
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Pop (remove) the first element from list
*/

#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.h"
#include "linkedlist.c"

// Prototype declaration
int pop(node** head);

// Test client
int main() {

    // Create empty linked list
    node* test = create();

    /* Insert elements into linked list
       List is 5 -> 3 -> 10 -> 1 */
    insert(&test, 1);
    insert(&test, 10);
    insert(&test, 3);
    insert(&test, 5);

    /* Simple test cases
       Results should be :
            Length of list before: 4
            1st popped is 5
            2nd popped is 3
            Length of list after: 2
    */
    printf("Length of list before: %i\n", length(&test));
    printf("Popped element is %i\n", pop(&test));
    printf("Popped element is %i\n", pop(&test));
    printf("Length of list after: %i\n", length(&test));
    destroy(&test);

}

// Remove the first element and return the value
int pop(node** head) {

    // Exit if length of list is 0
    if (length(head) == 0) {
        printf("Can't perform pop on empty list\n");
        exit(1);
    }

    // Hold pointer to head of list
    node* popped = *head;
    
    // Store value at head of list
    int value = popped -> data;

    // Update head of list and free popped node
    *head = popped -> next;
    free(popped);

    // Return popped value
    return value;
}