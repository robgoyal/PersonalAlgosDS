#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

// Head of llist
typedef struct sllist
{
    int val;
    struct sllist* next;
} sllnode;

sllnode* head;

sllnode* create(int val) {
    sllnode *llist = malloc(sizeof(sllnode));
    if (llist != NULL) {
        llist->val = val;
        llist->next = NULL;
    }

    head = malloc(sizeof(sllnode));
    if (head != NULL) {
        head = llist;
    }   

    return llist;
}

sllnode* insert(sllnode* head, int val) {
    sllnode* node = malloc(sizeof(sllnode));
    node->val = val;
    node->next = head;
    head = node;
    return head;
}

bool find(sllnode* head, int val) {
    sllnode* traverse = head;
    while (traverse->next != NULL) {
        if (traverse->val == val) {
            return true;
        }
        else {
            traverse = traverse->next;
        }
    }
    return false;
}

void destroy(sllnode* head) {

    sllnode* current = malloc(sizeof(sllnode));
    current = head;
    sllnode* next = malloc(sizeof(sllnode));

    while (current != NULL) {
        next = current -> next;
        free(current);
        current = next;
    }
    head->next = NULL;
}


int main() {
    sllnode* new = create(6); 
    new = insert(new, 5);
    new = insert(new, 12);
    printf("Node value: %i\n", new->next->next->val);
    printf("Number exists: %i\n", find(new, 4));
    destroy(new);
}