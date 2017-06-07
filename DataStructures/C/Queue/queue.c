/* Name: Queue.c
   Author: Robin Goyal
   Last-Modified: June 7, 2017
   Purpose: Create a queue using linked lists. This implementation
            holds a tail pointer and head pointer for O(1) enqueuing
            and dequeuing. 
*/

#include "queue.h"

queue* create() {
    queue* queue = malloc(sizeof(queue));
    queue -> head = NULL;
    queue -> tail = NULL;

    return queue;
}

void enqueue(queue** queue, int val) {
    node* node = malloc(sizeof(node));

    if (node == NULL) {
        printf("Memory was not allocated properly. Exiting!");
        exit(1);
    }

    node -> data = val;
    node -> next = NULL;

    if ((*queue) -> tail == NULL) {
        (*queue) -> tail = node;
        (*queue) -> head = (*queue) -> tail;
    }

    else {
        (*queue) -> tail -> next = node;
        (*queue) -> tail = node;
    }

}

int dequeue(queue** queue) {
    if (length <= 0) {
        printf("No values in queue");
        exit(1);
    }

    node* dequeued = (*queue) -> head;
    int value = dequeued -> data;
    (*queue) -> head = (*queue) -> head -> next;
    free(dequeued);

    return value;
}


int length(queue** queue) {
    node* current = (*queue) -> head;

    int count = 0;
    while (current != NULL) {
        count++;
        current = current -> next;
    }

    return count;
}

void print(queue** queue) {
    node* traversal = (*queue) -> head;

    while (traversal != NULL) {
        printf("%i\n", traversal -> data);
        traversal = traversal -> next;
    }
}

void destroy(queue** queue) {
    node* traversal = (*queue) -> head;
    node * temp = NULL;

    while (traversal != NULL) {
        (*queue) -> head = (*queue) -> head -> next;
        free(traversal);
        traversal = (*queue) -> head;
    }

    (*queue) -> head = NULL;
    (*queue) -> tail = NULL;
}

int main(void) {
    queue* test = create();
    for (int i = 0; i < 10; i++) {
        enqueue(&test, i);
    }

    /*for (int i = 0; i < 10; i++) {
        printf("%i\n", dequeue(&test));
    }
*/    printf("%i\n", length(&test));
    destroy(&test);

    printf("%i\n", test -> head -> next -> data);
    /*printf("%i\n", length(&test));
    printf("%i\n", dequeue(&test));
    printf("%i\n", test -> head -> data);*/
}