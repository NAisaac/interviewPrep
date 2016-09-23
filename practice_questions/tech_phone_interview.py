"""
*** Fibonacci number ***
Given the n calculate the nth Fibonacci number
"""

def fib(n):
	if n == 0:
		return 0
	elif n == 1:
		return 1
	else:
		return fib(n-1) + fib(n-2)

# print 5
print(fib(5))
# print 13
print(fib(7))
# print 55
print(fib(10))

"""
*** Histogram ***
 Counts the frequency of each unique number occurring in the array and
 returns the output as a string with the unique numbers in ascending sorted
 order next to their counts.  e.g. for {1,30,1,1,5,12,5} the expected output
 would be "1:3, 5:2, 12:1, 30:1, etc."
"""

def hist(input_array):
	hist_dict = {}
# Populate the dictionary
	for i in input_array:
		if i in hist_dict:
			hist_dict[i] += 1
		else:
			hist_dict[i] = 1

# Sort the dictionary by key put it into a list
	ord_hist_list = sorted(hist_dict.items())

# Print the elements on the same line
	for j in ord_hist_list:
		print "%d:%d" %(j[0], j[1]),

blah = [30, 1, 5, 1, 1, 5, 12]
hist(blah)

"""
*** Division w/o a Divider ***
Takes two integers and prints the quotient and the remainder using only plus and minus as arithmetic operators
"""

def basic_divider(number, divider):
	quotient = 0
	while number > divider:
		number -= divider
		quotient += 1
	remainder = number
	print "Quotient: %d and Remainder: %d" %(quotient, remainder)

basic_divider(11, 2)


