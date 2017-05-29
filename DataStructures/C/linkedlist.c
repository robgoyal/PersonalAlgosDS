/* Name: linkedlist.c 
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Create a linked list data structure for personal
            use and learning
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "linkedlist.h"

// Initialize node pointer head and set to NULL
node* create() {
    node* head = NULL;

    return head;
}

// Insert new element to the front of the linked list for O(1) operation
void insert(node** head, int val) {

    // Allocate memory for new node and check for failure
    node* node = malloc(sizeof(node));

    if (node == NULL) {
        printf("Memory was not allocated properly. Exiting. ");
        exit(1);
    }

    // Set new nodes next node pointer to null if list is empty
    if (*head == NULL) {
        node -> next = NULL;
    }

    else {
        node -> next = *head;
    }

    // Initialize node data and set head to new node
    node -> data = val;       
    *head = node;
}

// Find val in linked list, O(n) operation
bool find(node** head, int val) {

    // Create traversal pointer
    node* current = *head;

    // Traverse through linked list until end is reached
    while (current != NULL) {

        // Check if current node data is val otherwise go to next node
        if (current -> data == val) {
            return true;
        }
        else {
            current = current -> next;
        }
    }

    return false;
}

// Destroy linked list freeing all allocated memory
void destroy(node** head) {

    // Create traversal pointer and temporary pointer
    node* current = *head;
    node* temp = NULL;

    // Traverse through linked list until end is reached
    while (current != NULL) {

        // Free nodes iteratively
        temp = current -> next;
        free(current);
        current = temp;
    }

    // Set caller function list pointer to NULL
    *head = NULL;
}