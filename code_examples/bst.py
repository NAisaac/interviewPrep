"""
Binary Search Tree:

For each node, left is less than the node's value and right is greater than the node's value
When searching through the tree, by comparing the node's value to the search value, we know 
which direction down the tree to go
"""


class Node(object):
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class BST(object):
	def __init__(self, root):
		self.root = Node(root)

	def insert(self, new_val):
		return self.insert_bst(self.root, new_val)

	def insert_bst(self, start, new_val):
		if start.value < new_val:
			if start.right:
				return self.insert_bst(start.right, new_val)
			else:
				start.right = Node(new_val)
		else:
			if start.left:
				return self.insert_bst(start.left, new_val)
			else:
				start.left = Node(new_val)

	def search(self, find_val):
		return self.search_bst(self.root, find_val)

	def search_bst(self, start, find_val):
		if start: 
			if start.value == find_val:
				return True 
			elif start.value < find_val:
				return self.search_bst(start.right, find_val)
			else:
				return self.search_bst(start.left, find_val) 
		else:
			return False


# Set up tree
tree = BST(4)

# Insert elements
tree.insert(2)
tree.insert(1)
tree.insert(3)
tree.insert(5)

# Check search
# Should be True
print tree.search(4)
# Should be False
print tree.search(6)
