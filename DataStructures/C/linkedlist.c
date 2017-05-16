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

void insert(node** head, int val) {
    // Allocate memory for new node and check for failure
    node* node = malloc(sizeof(node));
    if (node == NULL) {
        printf("Memory was not allocated properly. Exiting. ");
        exit(1);
    }

    if (*head == NULL) {
        node -> next = NULL;
    }

    else {
        node -> next = *head;
    }

    node -> data = val;   
    *head = node;            // Set head to new node
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

int main() {
    node* new = create(); 
    insert(&new, 3);
    insert(&new, 16);
    printf("Node value: %i\n", new->next->data);
    printf("Number exists: %i\n", find(new, 3));
    destroy(new);
}