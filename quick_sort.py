# http://www.geekviewpoint.com/python/sorting/quicksort
# https://github.com/blakeembrey/code-problems/blob/master/solutions/python/quick-sort.py

"""
Quicksort works by selecting an element called a pivot and splitting
the list around that pivot and make all the elements in, say, the
left sublist are less than pivot and all the elements in the right
sublist are greater than pivot. Apply the same recursively on the
left sublist and the right sublist until the sublist is 1 element long.
At this point sorting is done!
"""

from random import randint

def quickSort(lst):
	# List of 1 element is already sorted
	if len(lst) <= 1:
		return lst
	else:
		# Pivot can be chosen randomly
		pivotIndex = randint(0, len(lst)-1)
		# Elements lower than and greater than pivot
		lesser, greater = [], []
		for i in range(len(lst)):
			# Don't do anything if you're at the pivot
			if i == pivotIndex:
				pass
			else:
				# Sort elements into < pivot and >= pivot
				if lst[i] < lst[pivotIndex]:
					lesser.append(lst[i])
				else:
					greater.append(lst[i])
		# Recursively sort lesser and greater, concatenate results
		return quickSort(lesser) + [pivot] + quickSort(greater)