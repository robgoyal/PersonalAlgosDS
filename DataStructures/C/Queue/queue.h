/* Name: Queue.h
   Author: Robin Goyal
   Last-Modified: June 5, 2017
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

typedef struct Queue {
    node* head;
    node* tail;
} queue;

// Create empty queue
queue* create();

// Enqueue
void enqueue(queue** queue, int val);

// Dequeue
int dequeue();

// Print queue
void print();

// Length of queue
int length();

// Destroy
void destroy();

#endif /* QUEUE_H */