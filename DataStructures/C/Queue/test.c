/* Name: Test.c
   Author: Robin Goyal
   Last-Modified: June 7, 2017
   Purpose: Test the queue data structure
*/

#include "queue.c"

// Test client
int main(void) {

    // Create test queue
    queue* q = create();

    // Enqueue 1 to 10
    for (int i = 0; i < 10; i++) {
        enqueue(&q, i);
    }

    // Dequeue first 5 elements
    for (int i = 0; i < 5; i++) {
        dequeue(&q);
        enqueue(&q, 15 - i);
    }

    // This should print 5, 6, 7, 8, 9, 15, 14, 13, 12, 11
    print(&q);

    // Freeing memory
    destroy(&q);
}