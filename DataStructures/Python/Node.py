# Name: Node.py
# Author: Robin Goyal
# Last-Modified: January 4, 2018
# Purpose: Implement the node class for future data structure objects


class Node:

    # Provide default value of None if no next Node is provided
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __repr__(self):
        return "Node({}, {})".format(self.data, self.next)
