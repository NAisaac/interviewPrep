### http://visualgo.net/sorting
# Good GIF: https://en.wikipedia.org/wiki/Merge_sort
# Interactive Merge Sort: http://interactivepython.org/runestone/static/pythonds/SortSearch/TheMergeSort.html

"""
#Pseudocode

1. Divide the unsorted list containing n elements into n sublists
2. MergeSort these sublists to produce new sorted sublists until there is only 1 sublist remaining

*** MergeSort list A & list B into list C ***

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