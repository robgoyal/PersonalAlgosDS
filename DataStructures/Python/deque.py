# ----------------------- #
# Deque Class
# An abstract data type to be used in future programs
# Written and Coded by Robin Goyal

class Deque():
	'''
	An ordered collection of items 
	where items can be added to the
	front or the back.
	'''

	# Initialize a new deque and return the empty list
	def __init__(self):
		self.data = []
		return self.data

	# Adds a new item to the front of the deque
	def addFront(self, item):
		self.data.append(item)

	# Adds a new item to the end of the deque
	def addRear(self, item):
		self.data.insert(0, item)

	# Remove and return the item at the front of the deque
	def removeFront(self):
		return self.data.pop()

	# Remove and return the item and the end of the deque
	def removeRear(self):
		return self.data.pop(0)

	# Return the condition on an empty list
	def isEmpty(self):
		if size() == 0:
			return True
		else:
			return False

	# Return the size of the deque
	def size(self):
		return len(self.data)
