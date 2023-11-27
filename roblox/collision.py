def solution(grid):

	nR = len(grid)
	nC = len(grid[0])

	newGrid = [["0" for i in range(nC)] for j in range(nR)]

	for i in range(nR):
		isCol = False
		if 'A' in grid[i] and 'B' in grid[i] and grid[i].index('A') < grid[i].index('B'):
			isCol = True

		else: 
			if'A' in grid[i]:
				indexA = grid[i].index('A')
				for k in range(indexA, nC-1):
					if newGrid[i][k] != 'X':
						newGrid[i][k] = '0'
				newGrid[i][nC-1] = 'A'

			if 'B' in grid[i]:
				indexB = grid[i].index('B')
				for k in range(1, indexB+1):
					if newGrid[i][k] != 'X':
						newGrid[i][k] = '0'
				newGrid[i][0] = 'B'
			for j in range(nC):
				if newGrid[i][k] != 'X':
					newGrid[i][k] = grid[i][j]
