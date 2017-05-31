/* Name: insertNth.c
   Author: Robin Goyal
   Last-Modified: May 31, 2017
   Purpose: Insert an element at the Nth index
*/

#include <stdio.h>
#include <stdlib.h>
#include "linkedlist.c"
#include "linkedlist.h"

// Prototype declaration
void insertNth(node** head, int index, int val);

// Test Client
int main() {

    // Create empty linked list
    node* test = create();

    // Insert elements into linked list
    for (int i = 0; i < 5; i++) {
        insertNth(&test, i, i + 5);
    }
    for (int i = 0; i < 5; i++) {
        insertNth(&test, i + 3, i + 15);
    }

    // Print contents of linked list
    print(&test);
    destroy(&test);
}

// Insert element at Nth index of linked list
void insertNth(node** head, int index, int val) {

    // Exit function if index is too great
    if (index > length(head)) {
        printf("Index too large. Max index is %i\n", length(head));
        return;
    }

    // Use insert function if inserting at front of list
    if (index == 0) {
        insert(head, val);
        return;
    }

    // Create traversal pointer
    node* current = *head;
    for (int i = 0; i < index - 1; i++) {
        current = current -> next;
    }

    // Allocate memory for new node
    node* node = malloc(sizeof(node));

    // Insert node and update pointers
    node -> data = val;
    node -> next = current -> next;
    current -> next = node;

}