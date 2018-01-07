# Name: LList.py
# Author: Robin Goyal
# Last-Modified: January 5, 2018
# Purpose: Implement ADT for Linked List

from Node import Node


class LinkedList:

    def __init__(self):
        self.head = None
        self.length = 0

    def add(self, item):
        '''
        item -> any: data to add to the list in the form of a Node
        return -> nothing

        Assumption -> Add Node to the front of the linked list
        '''

        if self.head is None:
            self.head = Node(item)
        else:
            temp = Node(item, self.head)
            self.head = temp

        self.length += 1

    def remove(self, item):
        '''
        item -> any: item to remove from Linked List
        return -> nothing

        Assumption -> Item exists in list
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

        return self.length

    def append(self, item):

        temp = Node(item)

        if self.head is None:
            self.head = temp

        else:
            traversal = self.head

            while (traversal.getNext() is not None):
                traversal = traversal.getNext()

            traversal.setNext(temp)

        self.length += 1

    def __str__(self):
        '''
        return -> str: prints the data of the linked list
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


if __name__ == "__main__":
    test = LinkedList()
    test.add(5)
    test.add(7)
    test.add("Hello")
    test.add(8)
    test.add(5.5)
    test.add(True)
    test.append(16)

    test2 = LinkedList()
    test2.append(5)
    print(test2)
    # print(test)
    # test.remove(8)
    # print(test)
    # test.remove(5)
    # print(test)

    print(test.size())
