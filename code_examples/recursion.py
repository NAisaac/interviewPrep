"""
Recursion simply put has 2 parts:
1. Base case
2. Calling itself

In the Fibonacci series (0, 1, 1, 2, 3, 5, 8, 13, 21, 34...) it all comes down to decomposing the number to... 

Fib(0) = 0
Fib(1) = 1

After that is just adding the previous two numbers
"""

# Iterative way
def iterativeFib(position):
	if (position == 0): 
		return 0
	if (position == 1): 
		return 1

	first = 0
	second = 1
	next = first + second;
	for i in range(2, position):
		first = second
		second = next
		next = first + second
	}
	return next
}

# Recursive way
def recursiveFib(position):
	if position == 0: 
		return 0
	elif position == 1: 
		return 1
	else:
		return recursiveFib(position-1) + recursiveFib(position-2)