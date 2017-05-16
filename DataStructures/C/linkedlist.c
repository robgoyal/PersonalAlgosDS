/* Name: linkedlist.c 
   Author: Robin Goyal
   Last-Modified: May 16, 2017
   Purpose: Create a linked list data structure for personal
            use and learning
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#include "linkedlist.h"

node* head;

node* create() {

    head = NULL;

    return head;
}

node* insert(node* head, int val) {
    // Allocate memory for new node and check for failure
    node* node = malloc(sizeof(node));
    if (node == NULL) {
        printf("Memory was not allocated properly. Exiting. ");
        exit(1);
    }

    node -> data = val;   
    node -> next = head;    // Link to head of list

    head = node;            // Set head to new node
    return head;
}

bool find(node* head, int val) {

    node* current = head;

    while (current -> next != NULL) {
        if (current -> data == val) {
            return true;
        }
        else {
            current = current -> next;
        }
    }
    return false;
}

void destroy(node* head) {

    node* current = head;
    node* temp = NULL;
    while (current -> next != NULL) {
        temp = current;
        current = current -> next;
        free(temp);
    }
    free(current);
}
