#--------------------------------#
# Stack Class
# An abstract data type to utilize in future programs when necessary
# Written and Coded by Robin Goyal
#--------------------------------#

class Stack:

	def __init__(self):
		self.data = []
		self.len = 0
		return self.data

	def push(self, item):
		self.data.append(item)
		self.len = self.len + 1

	def pop(self):
		if(!(isEmpty()):
			self.len = self.len - 1	
			return self.data.pop(self.len)

	def peek(self):
		if !(isEmpty()):
			return self.data[self.len - 1]

	def isEmpty(self):
		if self.len == 0:
			return True

	def size(self):
		return self.len
