# Name: LList.py
# Author: Robin Goyal
# Last-Modified: January 9, 2018
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

        if self.getLength() == 0:
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

        return self.getLength()

    def append(self, item):
        '''
        item -> any type

        Add item to end of list
        '''

        temp = Node(item)

        # Point head to new node if list is empty
        if self.getLength() == 0:
            self.head = temp

        else:
            traversal = self.head

            # Traverse through list until reaching final node
            while (traversal.getNext() is not None):
                traversal = traversal.getNext()

            # Set the next pointer of the final node to the new node
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

    def insert(self, pos, item):
        '''
        item -> any type
        pos -> int: position to insert item at

        Assumption -> pos < self.length
                      item is not in the list
                      pos is zero-indexed
        '''

        # Insert element at front of list
        if pos == 0:
            self.add(item)

        else:
            traversal = self.head

            # Traverse through list until reaching desired position
            while (pos > 1):
                traversal = traversal.getNext()
                pos -= 1

            # Insert node at desired position
            temp = Node(item, traversal.getNext())
            traversal.setNext(temp)

    def pop(self, pos=None):
        '''
        pos -> int: index of element, None if no argument is passed
        return -> any type: last item in list

        Assumption -> pos is a valid integer between 0 and length of list - 1
        Remove and return the final item in the list
        '''

        traversal = self.head

        # Remove first element if argument is 0th index or length of list is 1
        if self.getLength() == 1 or pos == 0:
            data = traversal.getData()
            self.head = traversal.getNext()

        # Remove last element if no argument is passed or argument is the final index
        elif pos is None or pos == self.getLength() - 1:
            while (traversal.getNext().getNext() is not None):
                traversal = traversal.getNext()

            data = traversal.getNext().getData()
            traversal.setNext(None)

        # Remove element by traversing to desired index and remove element
        else:
            while (pos > 1):
                traversal = traversal.getNext()
                pos -= 1

            data = traversal.getNext().getData()
            traversal.setNext(traversal.getNext().getNext())

        # Decrement length of list
        self.length -= 1

        # Return data of removed node
        return data

    def getLength(self):
        '''
        return -> int

        Returns the length of the list
        '''

        return self.length

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
