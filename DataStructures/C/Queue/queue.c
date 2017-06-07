/* Name: Queue.c
   Author: Robin Goyal
   Last-Modified: June 7, 2017
   Purpose: Create a queue using linked lists. This implementation
            holds a tail pointer and head pointer for O(1) enqueuing
            and dequeuing. 
*/

#include "queue.h"

// Create queue 
queue* create() {

    // Allocate memory for queue
    queue* queue = malloc(sizeof(queue));
    queue -> head = NULL;
    queue -> tail = NULL;

    return queue;
}

// Add element to end of queue
void enqueue(queue** queue, int val) {

    // Allocate memory for new node
    node* node = malloc(sizeof(node));

    // Check if memory was properly allocated
    if (node == NULL) {
        printf("Memory was not allocated properly. Exiting!");
        exit(1);
    }

    // Initialize node members
    node -> data = val;
    node -> next = NULL;

    // Point head and tail to new node if empty queue
    if ((*queue) -> tail == NULL) {
        (*queue) -> tail = node;
        (*queue) -> head = (*queue) -> tail;
    }

    // Point tail to next node and update tail
    else {
        (*queue) -> tail -> next = node;
        (*queue) -> tail = node;
    }

}

// Remove element from front of queue
int dequeue(queue** queue) {

    // Check if queue isn't empty
    if (length <= 0) {
        printf("No values in queue");
        exit(1);
    }

    // Point to head of queue
    node* dequeued = (*queue) -> head;

    // Hold value of front element of queue
    int value = dequeued -> data;

    // Point head to next element in queue and free memory
    (*queue) -> head = (*queue) -> head -> next;
    free(dequeued);

    return value;
}


// Calculate length of queue
int length(queue** queue) {

    // Create traversal pointer
    node* traversal = (*queue) -> head;

    int count = 0;

    // Increment count for each element until end is reached
    while (traversal != NULL) {
        count++;
        traversal = traversal -> next;
    }

    return count;
}

// Print elements of queue
void print(queue** queue) {

    // Create traversal pointer
    node* traversal = (*queue) -> head;

    // Print each element until end is reached
    while (traversal != NULL) {
        printf("%i\n", traversal -> data);
        traversal = traversal -> next;
    }
}

// Free memory of queue structure
void destroy(queue** queue) {

    // Create traversal pointer
    node* traversal = (*queue) -> head;

    // Iterate through queue until end 
    while (traversal != NULL) {

        // Free each node memory
        (*queue) -> head = (*queue) -> head -> next;
        free(traversal);
        traversal = (*queue) -> head;
    }

    // Free queue struct memory
    free(*queue);
    (*queue) = NULL;
}