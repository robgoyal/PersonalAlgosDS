/* Name: linkedlist.h
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Defines node struct and prototypes
*/

#include <stdio.h> 
#include <stdlib.h>
#include <stdbool.h>

#ifndef LINKEDLIST_H_ /* Include guard */
#define LINKEDLIST_H_

// linked list structure definition
typedef struct sllist {
    int data;
    struct sllist* next;
} node;

// Creates an empty linked list
node* create();

// Inserts a val into the linked list
void insert(node** head, int val);

// Determines if value exists in linked list
bool find(node** head, int val);

// Destroys linked list
void destroy(node** head);

#endif // LINKEDLIST_H_