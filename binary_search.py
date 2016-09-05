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

Assume the list only has distinct elements, meaning there are no repeated values, 
and elements are in a strictly increasing order. 

Return the index of value, or -1 if the value
doesn't exist in the list.
"""

def binary_search(input_array, value):
	# loop until length is 1
	while len(input_array) > 1:
		# Find middle value or round down
		middle = len(input_array)/2
		# if value is equal to middle value; return that index
		if input_array[middle] == value:
			return middle
		# if value is greater than middle value; return remaining list
		elif input_array[middle] < value:
			input_array = input_array[middle+1:len(input_array)]
		# if value is less than middle value; return remaining list
		else:
			input_array = input_array[0:middle]
			

	# if last element matches value
	# else return -1


test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print binary_search(test_list, test_val1)
print binary_search(test_list, test_val2)