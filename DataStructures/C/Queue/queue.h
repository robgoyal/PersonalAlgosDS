/* Name: Queue.h
   Author: Robin Goyal
   Last-Modified: June 7, 2017
   Purpose: Define queue struct and protoype functions.
            Implemented on top of linked list
*/

#ifndef QUEUE_H
#define QUEUE_H

#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Define node for queue struct
typedef struct Node{
    int data;
    struct Node* next;
} node;

// Define Queue struct consisting of head node and tail node
typedef struct Queue {
    node* head;
    node* tail;
} queue;

// Create empty queue
queue* create();

// Add item to end of queue
void enqueue(queue** queue, int val);

// Remove item from front of queue
int dequeue(queue** queue);

// Print elements of queue
void print(queue** queue);

// Return length of queue
int length(queue** queue);

// Destroy and free memory of all queue elements
void destroy(queue** queue);

#endif /* QUEUE_H */