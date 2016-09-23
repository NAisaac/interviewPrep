""" 
Python's list (array) time complexity: https://wiki.python.org/moin/TimeComplexity

e.g. Inserting into a list is easy (happens in constant time). However, inserting into an array is O(n), since you may need to shift elements to make space for the one you're inserting, or even copy everything to a new array if you run out of space. Thus, inserting into a Python list is actually O(n).

Because of the above reason, LINKED LIST comes in handy, in which insertion takes O(1) instead of O(n) because
all you have to do is change the reference pointers
"""

class Element(object):
	def __init__(self, value):
		self.value = value
		self.next = None

# Establishing that a LinkedList is something that has a head Element, which is the first element 
# in the list. If we establish a new LinkedList without a head, it will default to None
class LinkedList(object):
	def __init__(self, head=None):
		self.head = head

# Add an Element object (new_element) to the end of LinkedList
	def append(self, new_element):
		current = self.head
		# If the LinkedList has a head, iterate through Elements until you reach the end of the list.
		# And then set next to be the new_element
		if self.head:
			while current.next:
				current = current.next
			current.next = new_element
		# If the LinkedList doesn't have a head, assign the new_element as the head
		else:
			self.head = new_element

# Get an element from a particular position. Assume the first position is "1". Return "None" if 
# position is not in the list
	def get_position(self, position):
	# Is position a valid number? does the head exist? does the current exist?
		if position < 1:
			return "None"
		current = self.head
		for i in range(1, position):
			if current:
				if i == position:
					return current
				else:
					current = current.next
			else: 
				return "None"

# Insert a new node at the given position. Assume the first position is "1". Inserting at position 
# 3 means between the 2nd and 3rd elements
	def insert(self, new_element, position):
	# Is it inserting before head? Is it inserting after head? Is the position even valid?
		if position == 1:
			new_element.next = self.head
			self.head = new_element
		elif position > 1:
			current = self.head
			for i in range(1, position-1):
				if i == position-1:
					new_element.next = current.next
					current.next = new_element
				else:
					current = current.next
		else:
			return "Position invalid"

# Delete the first node with a given value. Edge cases: only head exists OR the value doesn't exist
	def delete(self, value):
		current = self.head
		previous = None
		# Not only check for the value but also check if there is a next element
		while current.value != value and current.next:
			previous = current
			current = current.next
		if current.value == value:
			if previous == None:
				# only head exists
				self.head = current.next
			else:
				previous.next = current.next
		# value doesn't exist
		elif current.next == None:
			return "No node found with the given value"


