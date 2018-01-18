# Name: Deque.py
# Author: Robin Goyal
# Last-Modified: January 17, 2018
# Purpose: Implement ADT for Deque


from LList import LinkedList


class Deque(LinkedList):
    '''
    An implementation of a Deque with basic functionality.
    A deque allows you to add and remove nodes from both ends.
    It is similar to a linked list but

    Attributes:
        head: A pointer to point to the first node in deque
        _length: An integer representing the number of current items in the deque

    Inherited Methods in Deque ADT from Linked List:
        is_empty: Returns a boolean indicating if the Deque is empty or not
        size: Returns an integer indicating the number of items in the Deque
    '''

    def __init__(self):
        '''
        Initializes an empty deque with no items

        Inherited Attributes:
            - head
            - _length
        '''

        LinkedList.__init__(self)

    def add_front(self, item):
        '''
        item -> any type: data to add to the front of the deque

        Adds an item to the front of the deque. This functionality
        is the same as the add() method defined in the LinkedList class.

        Examples:
            - add_front(-6.7): 1 -> True ===> -6.7 -> 1 -> True
            - add_front(5): Empty Deque ===> 5
        '''

        LinkedList.add(self, item)

    def add_rear(self, item):
        '''
        item -> any type: data to add to the end of the deque

        Adds an item to the end of the deque. This functionality
        is the same as the append() method defined in the LinkedList class.

        Examples:
            - add_rear(5): 2 -> 3.5 ===> 2 -> 3.5 -> 5
            - add_rear(12): Empty Deque ===> 12
        '''

        LinkedList.append(self, item)

    def remove_front(self):
        '''
        return -> any type: first item in deque

        Removes the first item in the Deque and returns it. The
        functionality is similar to the pop() method defined in
        the LinkedList class except an argument of 0 is required.

        Examples:
            - remove_front(): 5 -> 2 -> 3 ===> 5 (returned value)
                              2 -> 3 (modified Deque)
            - remove_front(): 2 ===> 2 (returned value)
                              Empty Deque (modified Deque)
        '''

        return LinkedList.pop(self, 0)

    def remove_rear(self):
        '''
        return -> any type: last item in deque

        Removes the last item in the deque and returns it. The
        functionality is the same as the pop() method defind in
        the LinkedList class.

        Examples:
            - remove_rear(): 2 -> True -> False ===> False (returned value)
                             2 -> True (modifed Deque)
            - remove_rear(): True -> 3.4 ===> 3.4 (returned value)
                             3.4 (modified Deque)
        '''

        return LinkedList.pop(self)
