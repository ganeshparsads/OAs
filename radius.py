
matrix = [
	[0, 0, 0],
	[0, 255, 0],
	[0, 0, 0]
]

new_matrix = []

def find_neighbors(i, j, matrix, m, n, r):
	dirs = []

	if i == 1 and j == 1:
		import pdb
		pdb.set_trace()

	for i in range(-r, r+1):
		for j in range(-r, r+1):
			if not (i == 0 == j == 0):
				dirs.append((i, j))

	# print(dirs)
	eles = []

	for d in dirs:
		new_row = d[0] + i
		new_col = d[1] + j

		if 0 <= new_row < m and 0 <= new_col < n:
			eles.append(matrix[new_row][new_col])
	# import pdb
	# pdb.set_trace()
	print(dirs)
	print(eles)
	mean = sum(eles) // len(eles)
	return mean

m = len(matrix)
n = len(matrix[0])

radius = 2

for i in range(m):
	temp = []
	for j in range(n):
		mean = find_neighbors(i, j, matrix, m, n, radius)
		temp.append((matrix[i][j] + mean)//2)

	new_matrix.append(temp)

print(new_matrix)
