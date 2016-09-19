"""

Given a 2D matrix of arrays of 0s and 1s, find the # of islands
An island consists of 1s connected horizontally or vertically
Optional: what if diagonal connection counts? 

*** Graphs - BFS ***

"""

def islandCounter(M):
	if (M == None or M == [[]]):
		return 0
	islands = 0
	row = len(M)
	col = len(M[0])
	for i in range(0, row):
		for j in range(0, col):
			if (M[i][j] == 1):
				islands += 1
				findPartsOfIsland(M, i, j, row, col)

# use a helper method (aka abstraction) which does BFS graph search

