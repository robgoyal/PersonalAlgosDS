#include <stdio.h> 
#include <stdlib.h>
#include <stdbool.h>

#ifndef LINKEDLIST_H_ /* Include guard */
#define LINKEDLIST_H_

typedef struct sllist
{
    int val;
    struct sllist* next;
} sllnode;

sllnode* create(int val);

sllnode* insert(sllnode* head, int val);

bool find(sllnode* head, int val);

void destroy(sllnode* head);

#endif // LINKEDLIST_H_