"""
Write a function that spiral prints a matrix (a list of lists)

Given a list of lists ...
[[1,2,3,4],
 [5,6,7,8],
 [9,10,11,12],
 [13,14,15,16]]
the function prints ...
1 2 3 4 8 12 16 15 14 13 9 5 6 7 11 10
"""
import pdb

def spiralPrint(matrix):
	output = []
	# initialize index trackers to help reduce the matrix
	col_start = 0
	col_finish = len(matrix[0]) - 1
	row_start = 0
	row_finish = len(matrix) - 1

	# 4 functions taking matrix and 4 index range arguments: h_start, h_finish, v_start, v_finish
	while matrix:
		if row_start > row_finish:
			break
		else:
			## print right
			for a in range(col_start, col_finish + 1):
				output.append(matrix[row_start][a])
			# reduce the matrix
			row_start = row_start + 1
		if col_start > col_finish:
			break
		else:
			# print down
			for b in range(row_start, row_finish + 1):
				output.append(matrix[b][col_finish])
			# reduce the matrix
			col_finish = col_finish - 1
		if row_start > row_finish:
			break
		else:
			# print left
			for c in range(col_finish, col_start - 1, -1):
				output.append(matrix[row_finish][c])
			# reduce the matrix
			row_finish = row_finish - 1
		if col_start > col_finish:
			break
		else:
			# print up
			for d in range(row_finish, row_start - 1, -1):
				output.append(matrix[d][col_start])
			# reduce the matrix
			col_start = col_start + 1

	return output


theInput = [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]]
print(spiralPrint(theInput))

theInput = [[1,2,3],[5,6,7],[9,10,11],[13,14,15]]
print(spiralPrint(theInput))

