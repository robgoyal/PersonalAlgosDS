#--------------------------------#
# Stack Class
# An abstract data type to utilize in future programs when necessary
# Written and Coded by Robin Goyal
#--------------------------------#

class Stack:
	''' 
	The stack data structure is a ordered
	collection of items where the items 
	can be added and only the top most 
	element can be removed. This is a 
	Last In First Out order. 
	'''

	# Initialize data and returns empty stack
	def __init__(self):
		self.data = []
		return self.data

	# Push item onto the stack
	def push(self, item):
		self.data.append(item)

	# Pop and return top most item of the stack
	def pop(self):
		return self.data.pop()

	# Return top most item of the stack
	def peek(self):
		return self.data[size() - 1]

	# Check if stack is empty
	def isEmpty(self):
		if len(self.data) == 0:
			return False
		else:
			return True

	# Return the size of the stack
	def size(self):
		return len(self.data)
