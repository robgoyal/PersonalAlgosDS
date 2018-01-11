# Name: Node.py
# Author: Robin Goyal
# Last-Modified: January 5, 2018
# Purpose: Implement the node class for future data structure objects


class Node:

    # Provide default value of None if no next Node is provided
    def __init__(self, data, next_node=None):
        self._data = data
        self._next = next_node

    # Getters
    def get_data(self):
        '''
        return -> any: data of Node
        '''

        return self._data

    def get_next(self):
        '''
        return -> Node: Returns next Node if it exists, otherwise None
        '''

        return self._next

    # Setters
    def set_data(self, data):
        '''
        data -> any: data to modify of current Node
        '''

        self._data = data

    def set_next(self, next_node):
        '''
        next -> Node: modify pointer to new next Node
        '''

        self._next = next_node

    def __repr__(self):
        return "Node({}, {})".format(self._data, self._next)
