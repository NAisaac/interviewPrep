"""
Python lists have a method called index(), which just does a search and returns the first index with an 
instance of that value. Next, you're going to write a binary search function that has the same result, 
but searches faster. 
"""

"""
You're going to write a binary search function. You should use an iterative approach - meaning
using loops. Your function should take two inputs: 

1. a Python list to search through
2. the value you're searching for

*** ASSUMPTION: the list only has distinct elements, meaning there are no repeated values ***

Return the index of value, or -1 if the value doesn't exist in the list.
"""

def binary_search(input_array, value):
	top_index = len(input_array) - 1
	bottom_index = 0
	# loop until we've narrowed our search down to 2 elements
	while (top_index - bottom_index) > 1:
		# Find middle index
		middle_index = (top_index+bottom_index)/2
		# if value is equal to middle value; return that index
		if input_array[middle_index] == value:
			return middle_index
		# if value is greater than middle value; return new top_index and bottom_index
		elif input_array[middle_index] < value:
			bottom_index = middle_index + 1
		# if value is less than middle value; return new top_index and bottom_index
		else:
			top_index = middle_index - 1

	# Once narrowed down to 2 elements
	if input_array[top_index] == value:
		return top_index
	elif input_array[bottom_index] == value:
		return bottom_index
	else:
		return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
test_val3 = 11
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)
print binary_search(test_list, test_val3)

