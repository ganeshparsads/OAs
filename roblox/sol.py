from collections import Counter


# matrix = [
# 	[2, 0, 0, 0, 2],
# 	[1, 2, 1, 2, 0],
# 	[0, 1, 2, 1, 0],
# 	[0, 0, 2, 1, 1],
# 	[1, 1, 2, 1, 1]
# ]
matrix = [
	[1, 0, 2],
	[1, 2, 0],
	[0, 2, 0]
]

def solution(matrix):
	n = len(matrix)

	diagonal_ele = []
	rest = []

	mid = n//2 + 1

	hSet = set()

	# import pdb
	# pdb.set_trace()
	for i in range(1, n+1):
		if i<mid:
			diagonal_ele.append(matrix[i-1][i-1])
			diagonal_ele.append(matrix[i-1][-1 - (i-1)])
			hSet.add(((i-1),(i-1)))
			hSet.add(((i-1),(n-1 - (i-1))))
		for j in range(1, n+1):
			if (i >= mid and j == mid):
				hSet.add(((i-1),(j-1)))
				diagonal_ele.append(matrix[i-1][j-1])
			elif((i-1, j-1) not in hSet):
				rest.append(matrix[i-1][j-1])
	print(hSet)
	print(len(diagonal_ele), ":", diagonal_ele)
	print(len(rest), ":", rest)

	dig_count = Counter(diagonal_ele)
	res_count = Counter(rest)

	max_d_count = max(list(dig_count.values()))
	max_r_count = max(list(res_count.values()))
	c1 = len(diagonal_ele) - max_d_count
	c2 = len(rest) - max_r_count
	print(c1)
	print(c2)
	print(c1+c2)

	return (c1+c2)

solution(matrix)