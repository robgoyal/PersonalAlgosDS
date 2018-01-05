# Name: Node.py
# Author: Robin Goyal
# Last-Modified: January 5, 2018
# Purpose: Implement the node class for future data structure objects


class Node:

    # Provide default value of None if no next Node is provided
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    # Getters
    def getData(self):
        '''
        return -> any: data of Node
        '''

        return self.data

    def getNext(self):
        '''
        return -> Node: Returns next Node if it exists, otherwise None
        '''

        return self.next

    # Setters
    def setData(self, data):
        '''
        data -> any: data to modify of current Node
        '''

        self.data = data

    def setNext(self, next):
        '''
        next -> Node: modify pointer to new next Node
        '''

        self.next = next

    def __repr__(self):
        return "Node({}, {})".format(self.data, self.next)
