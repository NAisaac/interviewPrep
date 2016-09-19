"""
Given a root of a Binary Search Tree and some value (x), find the largest value in the tree 
that is smaller than x

e.g. if an ordered list of all the values in the tree is {2, 3, 4, 7, 17, 19, 21, 35, 89}
and x is 19, the output of the function should be 17

Solution: BST_largest_smaller.pdf
"""

def findLargestSmaller(root, x):
	result = null
	while(root != null):
		if root.value > x:
			root = root.left
		"""
		It's important to understand why we always store the last key without comparing it 
		to the value stored beforehand: if we have stored a key before, we then chose to 
		continue its right sub-tree. Therefore, all following keys will always be larger than 
		and previously stored keys.
		"""
		elif root.value < x:
			result = root.value
			root = root.right
	return result