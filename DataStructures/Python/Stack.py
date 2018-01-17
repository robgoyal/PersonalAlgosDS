# Name: Stack.py
# Author: Robin Goyal
# Last-Modified: January 15, 2018
# Purpose: Implement ADT for Stack by inheriting from Linked List

from LList import LinkedList


class Stack(LinkedList):
    '''
    An implementation of a stack with necessary functionality.
    A stack is a LIFO (Last In First Out) data structure where
    elements can only be added from the front of the data structure.

    Attributes:
        head: A pointer to the first node in the stack
        _length: An integer representing the number of current items in the stack

    Inherited Methods in Stack ADT from Linked List:
        isEmpty: Returns a boolean indicating if the Stack is empty or not
        size: Returns the number of items in the Stack
    '''

    def __init__(self):
        '''
        Initializes an empty stack with no nodes.

        Inherited Attributes:
            - head
            - _length
        '''
        LinkedList.__init__(self)

    def push(self, item):
        '''
        item -> any type: data to add to the front of the stack
        return -> nothing

        Adds an item to the front of the stack. This functionality is
        the same as the add() method defined in the LinkedList class.

        Examples:
            - push(5): 2 -> 3 -> True ===> 5 -> 2 -> 3 -> True
            - push(-5.6): Empty Stack ===> -5.6
            - push(2.3): 4 ===> 2.3 -> 4
        '''

        LinkedList.add(self, item)

    def pop(self):
        '''
        return -> any type: first item in stack

        Removes the first item in the stack and returns it. The
        functionality is similar to the pop() method defined in the
        LinkedList class except an argument of zero is necessary.

        Examples:
            - pop(): 2 ===> 2 (returned value), Empty Stack (modified stack)
            - pop(): 5 -> True -> 6 ===> 5 (returned value), True -> 6 (modified stack)
        '''

        return LinkedList.pop(self, 0)

    def peek(self):
        '''
        return -> any type: first item in stack

        Assumption -> length of stack is at least 1.

        Returns the first item in the stack.

        Examples:
            - peek(): 5 -> 2 -> True ===> 5
            - peek(): 2 ===> 2
        '''

        return self.head.get_data()
