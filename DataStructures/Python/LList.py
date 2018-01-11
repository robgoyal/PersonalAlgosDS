# Name: LList.py
# Author: Robin Goyal
# Last-Modified: January 11, 2018
# Purpose: Implement ADT for Linked List

from Node import Node


class LinkedList:
    '''
    An implementation of a linked list with basic functionality
    to add Nodes to front of list, remove items, and additional
    functionality.

    Attributes:
        head: A pointer to point to the first node in the list
        __length: An integer representing the number of current items in the list
    '''

    def __init__(self):
        '''
        Initializes an empty list with no nodes
        '''

        self.head = None
        self._length = 0

    def add(self, item):
        '''
        item -> any type: data to add to the list in the form of a Node
        return -> nothing

        Add item to the front of the list.

        Examples:
            - add(5): Empty List ===> 5
            - add(16): 3 -> True -> 2 ===> 16 -> 3 -> True -> 2
        '''

        if self.get_length() == 0:
            self.head = Node(item)
        else:
            new_node = Node(item, self.head)
            self.head = new_node

        self._length += 1

    def remove(self, item):
        '''
        item -> any type: item to remove from list
        return -> nothing
        Assumption -> Item exists in list

        Remove an item from the list.

        Examples:
            - remove(5): 5 -> 3 -> 2 ===> 3 -> 2
            - remove(2.1): 61 -> 3 -> 2.1 ===> 61 -> 3
            - remove(False): 5 -> False -> 2 -> -5 ===> 5 -> 2 -> -5

        '''

        traversal_ptr = self.head

        # Check if item is at the front of the list
        if traversal_ptr.get_data() == item:
            self.head = traversal_ptr.get_next()

        else:
            # Traverse through list until locating the next node containing item
            while traversal_ptr.get_next().get_data() != item:
                traversal_ptr = traversal_ptr.get_next()

            # Check if item is at end of list
            if traversal_ptr.get_next().get_next() is None:
                traversal_ptr.set_next(None)

            # Item is in the middle of the list
            else:
                traversal_ptr.set_next(traversal_ptr.get_next().get_next())

        self._length -= 1

    def search(self, item):
        '''
        item -> any type: item to look for in the list
        return -> boolean

        Return a boolean indicating whether the item is in the list.

        Examples:
            - search(5): 5 -> 2 -> 1 ===> True
            - search(0): 5 -> 2 -> 1 ===> False
        '''

        traversal_ptr = self.head

        # Traverse through list
        while (traversal_ptr is not None):
            if traversal_ptr.get_data() == item:
                return True

            traversal_ptr = traversal_ptr.get_next()

        return False

    def isEmpty(self):
        '''
        return -> bool: Check if _length is 0

        Check whether the _length of the list is 0.

        Examples:
            - isEmpty(): 5 -> 2 ===> False
            - isEmpty(): Empty List ===> True
        '''

        return self.get_length() == 0

    def size(self):
        '''
        return -> int: length of list

        Returns the length of the list.

        Examples:
            - size(): 5 -> 2 ===> 2
            - size(): 5 ===> 1
            - size(): Empty List ===> 0

        '''

        return self.get_length()

    def append(self, item):
        '''
        item -> any type: node at add

        Add an item to the end of the list.

        Examples:
            - append(3): Empty List ===> 3
            - append(5): 3 -> 2 ==> 3 -> 2 -> 5
        '''

        new_node = Node(item)

        # Point head to new node if list is empty
        if self.get_length() == 0:
            self.head = new_node

        else:
            traversal_ptr = self.head

            # Traverse through list until reaching final node
            while (traversal_ptr.get_next() is not None):
                traversal_ptr = traversal_ptr.get_next()

            # Set the next pointer of the final node to the new node
            traversal_ptr.set_next(new_node)

        self._length += 1

    def index(self, item):
        '''
        item -> data: item to look for in list
        return -> int: position of item in list

        Assumption -> item is in list

        Return the index of the item in the list

        Examples:
            - index(5): 5 -> 2 -> 3 ===> 0
            - index(2): 25 -> True -> 1 -> 2 ===> 3
        '''

        traversal_ptr = self.head
        index = 0

        # Loop through list until item is found
        # Works off of the assumption that the item is in the list
        while (traversal_ptr.get_data() != item):
            index += 1
            traversal_ptr = traversal_ptr.get_next()

        return index

    def insert(self, pos, item):
        '''
        item -> any type
        pos -> int: position to insert item at

        Assumption -> pos < self._length
                      pos is zero-indexed

        Insert an item at pos in the list.

        Examples:
            - insert(0, 2): 1 -> 3 -> 16 ===> 2 -> 1 -> 3 -> 16
            - insert(3, 2): 1 -> 3 -> 16 ===> 1 -> 3 -> 16 -> 2
            - insert(2, 2): 1 -> 3 -> 16 ===> 1 -> 3 -> 2 -> 16
        '''

        # Insert element at front of list
        if pos == 0:
            self.add(item)

        else:
            traversal_ptr = self.head

            # Traverse through list until reaching desired position
            while (pos > 1):
                traversal_ptr = traversal_ptr.get_next()
                pos -= 1

            # Insert node at desired position
            new_node = Node(item, traversal_ptr.get_next())
            traversal_ptr.set_next(new_node)

    def pop(self, pos=None):
        '''
        pos -> int: index of element, None if no argument is passed
        return -> any type: last item in list

        Assumption -> pos is a valid integer between 0 and _length of list - 1

        Remove and return the final item in the list

        Examples:
            - pop(): 5 ===> 5
            - pop(0): 5 -> 3 -> 2 ===> 5
            - pop(): 5 -> 3 -> 2 ===> 2
            - pop(3): 5 -> 3 -> 2 -> 1 ===> 1
            - pop(2): 5 -> 3 -> True -> 2 ===> True
        '''

        traversal_ptr = self.head

        # Remove first element if argument is 0th index or _length of list is 1
        if self.get_length() == 1 or pos == 0:
            data = traversal_ptr.get_data()
            self.head = traversal_ptr.get_next()

        # Remove last element if no argument is passed or argument is the final index
        elif pos is None or pos == self.get_length() - 1:
            while (traversal_ptr.get_next().get_next() is not None):
                traversal_ptr = traversal_ptr.get_next()

            data = traversal_ptr.get_next().get_data()
            traversal_ptr.set_next(None)

        # Remove element by traversing to desired index and remove element
        else:
            while (pos > 1):
                traversal_ptr = traversal_ptr.get_next()
                pos -= 1

            data = traversal_ptr.get_next().get_data()
            traversal_ptr.set_next(traversal_ptr.get_next().get_next())

        # Decrement _length of list
        self._length -= 1

        # Return data of removed node
        return data

    def get_length(self):
        '''
        return -> int: length of list

        Getter for returning the length attribute.

        Examples:
            - get_length(): 5 -> 2 ===> 2
            - get_length(): 5 ===> 1
            - get_length(): Empty List ===> 0
        '''

        return self._length

    def __str__(self):
        '''
        return -> str

        Prints the data in each node of the linked list.

        Examples:
            The calls to __str__ are made by print function of instance of LinkedList
            - __str__(): 3 -> 4 -> 1 -> 3
            - __str__(): 1 -> 2
            - __str__(): 5
        '''

        traversal_ptr = self.head

        list_data = ""

        while (traversal_ptr is not None):

            # Remove arrow if looking at final element
            if traversal_ptr.get_next() is None:
                list_data += "{}".format(traversal_ptr.get_data())
            else:
                list_data += "{} -> ".format(traversal_ptr.get_data())

            traversal_ptr = traversal_ptr.get_next()

        return list_data
