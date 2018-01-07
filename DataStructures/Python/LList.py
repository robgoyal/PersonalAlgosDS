# Name: LList.py
# Author: Robin Goyal
# Last-Modified: January 7, 2018
# Purpose: Implement ADT for Linked List

from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, item):
        '''
        item -> any type: data to add to the list in the form of a Node
        return -> nothing

        Add item to the front of the list
        '''

        if self.head is None:
            self.head = Node(item)
        else:
            temp = Node(item, self.head)
            self.head = temp

        self.length += 1

    def remove(self, item):
        '''
        item -> any type: item to remove from list
        return -> nothing

        Assumption -> Item exists in list

        Remove item from the list
        '''

        traversal = self.head

        # Check if item is at the front of the list
        if traversal.getData() == item:
            self.head = traversal.getNext()

        # Traverse through list until the next node contains item
        else:
            while traversal.getNext().getData() != item:
                traversal = traversal.getNext()

            # Check if item is at end of list
            if traversal.getNext().getNext() is None:
                traversal.setNext(None)

            # Item is in the middle of the list
            else:
                traversal.setNext(traversal.getNext().getNext())

        self.length -= 1

    def search(self, item):
        '''
        item -> any type: item to look for in the list
        return -> boolean

        Return True or False whether item is in list
        '''

        traversal = self.head

        while (traversal is not None):
            if traversal.getData() == item:
                return True

            traversal = traversal.getNext()

        return False

    def isEmpty(self):
        '''
        return -> bool: Check if length is 0
        '''

        return self.length == 0

    def size(self):
        '''
        return -> int: length of list

        Return the length of the list
        '''

        return self.length

    def append(self, item):
        '''
        item -> any type

        Add item to end of list
        '''

        temp = Node(item)

        if self.head is None:
            self.head = temp

        else:
            traversal = self.head

            while (traversal.getNext() is not None):
                traversal = traversal.getNext()

            traversal.setNext(temp)

        self.length += 1

    def index(self, item):
        '''
        item -> data: item to look for in list
        return -> int: position of item in list

        Assumption -> item is in list

        Return the index of the item in the list
        '''

        traversal = self.head
        index = 0

        # Loop through list until item is found
        # Works off of the assumption that the item is in the list
        while (traversal.getData() != item):
            index += 1
            traversal = traversal.getNext()

        return index

    def __str__(self):
        '''
        return -> str

        Prints the data of the linked list
        '''

        traversal = self.head

        list_data = ""

        while (traversal is not None):

            # Remove arrow if looking at final element
            if traversal.getNext() is None:
                list_data += "{}".format(traversal.getData())
            else:
                list_data += "{} -> ".format(traversal.getData())

            traversal = traversal.getNext()

        return list_data
