# http://www.geekviewpoint.com/python/sorting/mergesort
# Good GIF: https://en.wikipedia.org/wiki/Merge_sort
# Interactive Merge Sort: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

"""
#Pseudocode

1. Divide the unsorted list containing n elements into n sublists
2. Merge these sublists to produce new sorted sublists until there is only 1 sublist remaining

*** mergeSort list A & list B into list C ***

while A and B is NOT empty:
	if head of A <= head of B:
		C.append(head of A)
		pop(head of A)
	else:
		C.append(head of B)
		pop(head of A)

## Once the above while loop finishes, either A or B will still have remaining elements

while A is NOT empty:
	C.append(head of A)
	pop(head of A)

while B is NOT empty:
	C.append(head of B)
	pop(head of B)
"""

def mergeSort(lst):
	# List of 1 element is already sorted
	if len(lst)<=1:
		return lst
	# split the lst into 2 sublists (left & right)
	mid = len(lst)/2
	left = lst[:mid]
	right = lst[mid:]
	# recursively split 
	A = mergeSort(left)
	B = mergeSort(right)

	return merge(A, B)

def merge(A, B):
	# takes in two sorted sublists and returns a merged sorted list
	if not A:
		return B
	if not B:
		return A
	if A[0] < B[0]:
		return [A[0]] + merge(A[1:], B)
	return [B[0]] + merge(A, B[1:])

lst = [54,26,93,17,77,31,44,55,20]
print(lst)
print(mergeSort(lst))
