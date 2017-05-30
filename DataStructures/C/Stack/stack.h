/* Name: stack.h
   Author: Robin Goyal
   Last-Modified: May 29, 2017
   Purpose: Define stack struct and prototypes. Implemented 
            on top of linked list
*/

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#ifndef STACK_H_ /* Include guard */
#define STACK_H_

typedef struct stack {
    int data;
    struct stack* next;
} node;

// Creates an empty stack
node* create();

// Pushes a value onto the stack
void push(node** head, int val);

// Return top value of stack
int top(node** head);

// Check if stack is empty 
bool isEmpty(node** head);

// Remove and return the top value of the stack
int pop(node** head);

// Destroy stack freeing all memory
void destroy(node** head);

#endif // STACK_H_ 