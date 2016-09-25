"""
two sum problem

e.g. 
Given an unsorted list, check if there are 2 numbers that sum to a specific number.
The list can be of zero, negative, and positive integers
"""
### Pseudocode
# Loop through the list
# 	create/add a dictionary from the given list dict{element:index}
# 	check if complement element exists in the dictionary
def twoSum(inputList, theSum):
	sumDict = {}
	for i in range(len(inputList)):
		sumDict[inputList[i]] = i
		theComplement = theSum - inputList[i]
		if theComplement in sumDict:
			print "%d and %d" %(theComplement, inputList[i])
			return True
	return False

a = [3, 4, 5, 6, 7, 8]
x = 15
print(twoSum(a,x))

"""
O(n) Method using Hash Table
For unsorted array, by using extra space we can solve the problem in O(n) time. 

* Time complexity is O(n) and the space complexity is O(n).

This solution runs in expected time O(n) because n insertions and n lookups in a
hash table takes expected time O(n). It uses space O(n). There is no clear way to 
improve on both the time complexity or the space complexity simultaneously.
"""