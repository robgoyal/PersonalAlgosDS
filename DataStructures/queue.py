# --------------------- #
# Queue Class
# An abstract data type to use in future programs
# Written and Coded by Robin Goyal

class Queue:
	'''
	The queue is a First In 
	First Out ordered collection
	of items where items can be added
	and only the bottom most element
	can be removed.
	''' 

	# Initialize data and return empty queue
	def __init__(self):
		self.data = []
		return self.data

	# Adds a new item to the end of the queue
	def enqueue(self, item):
		self.data.append(item)

	# Removes and returns the item from the front of the queue
	def dequeue(self):
		return self.data.pop(0)

	# Tests to see whether the queue is empty
	def isEmpty(self):
		if (size() == 0):
			return True
		else:
			return False

	# Returns the length of the queue
	def size(self):
		return len(self.data)