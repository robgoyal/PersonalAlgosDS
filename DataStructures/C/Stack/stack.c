/* Name: stack.c
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Create a stack data structure
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "stack.h"

// Create an empty linked list and return a pointer to head
node* create() {
    node* head = NULL;

    return head;
}

// Push a new element onto the stack
void push(node** head, int val) {

    // Allocate memory for a new node
    node* new_node = malloc(sizeof(node));

    // Check to make sure memory was allocated for node
    if (new_node == NULL) {
        printf("Memory was not allocated properly. Exiting!");
        exit(1);
    }

    // Set new node's next value to NULL if empty stack
    if (isEmpty(head)) {
        new_node -> next = NULL;
    }

    // Point to head if not empty
    else {
        new_node -> next = *head;
    }

    // Initialize node data to value and point head to node
    new_node -> data = val;
    *head = new_node;
}

// Remove and return top most element of stack
int pop(node** head) {

    // Verify stack isnt empty
    if (isEmpty(head)) {
        printf("Stack is empty. Exiting\n");
        exit(1);
    }

    // Create node pointer to hold pointer to head
    node* popped = *head;

    // Store value that is to be removed
    int value = popped -> data;

    // Point head to next node in stack and free popped node
    *head = popped -> next;
    free(popped);

    return value;
}

// Return value on top of stack
int top(node** head) {

    // Verify stack isn't empty
    if (isEmpty(head)) {
        printf("Stack is empty. Exiting!\n");
        exit(1);
    }

    return (*head) -> data;
}

// Return whether stack is empty
bool isEmpty(node** head) {

    // If head is set to NULL, then no values were pushed
    if (*head == NULL) {
        return true;
    }

    return false;
}

// Free all nodes in stack and set head pointer to NULL
void destroy(node** head) {

    // Traversal pointer
    node* current = *head;
    node* temp = NULL;

    // Traverse through stack until end is reached
    while (current != NULL) {

        // Free each node
        temp = current -> next;
        free(current);
        current = temp;
    }

    // Set caller pointee to NULL
    *head = NULL;
}