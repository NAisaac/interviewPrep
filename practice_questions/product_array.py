"""
Given an array of integers arr, write a function that returns another array at the same 
length where the value at each index i is the product of all array values except arr[i].
"""

def product_array(input_arr):
	front_arr = [0] * len(input_arr)
	back_arr = [0] * len(input_arr)
	for i in input_arr:
		if i == 0:
			front_arr[i] = 1
		else:
			front_arr[i] = front_arr[i-1] * input_arr[i-1]
	for j in range(len(input_arr)-1,0,-1):
		if j == len(input_arr) -1:
			back_arr[j] = 1
		else:
			back_arr[j] = back_arr[j+1] * input_arr[j+1]

	product_arr = [front[i] * back[i] for i in range(len(back_arr))]
	return product_arr

print(product_array([2,3,4,5]))