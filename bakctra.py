arr = [[1, 2, 3], [2, 1, 2], [3, 1, 1]]
n = 3

tR = len(arr)
tC = len(arr[0])

cnt = 0

cols = []
result = set()

for j in range(tC):
	each_col = []
	for i in range(tR):
		each_col.append(arr[i][j])

	cols.append(each_col)

def checkP(r1, r2, c1, c2):
	for i in range(r1, r2):
		for j in range(c1, c2):
			if arr[i][j] == 2:
				return True

	return False


def solution(r1, r2, c1, c2, n):
	global cnt
	global result
	# base 
	if n == 1:
		# import pdb
		# pdb.set_trace()
		if checkP(r1, r2, c1, c2):
			result.add((r1, r2, c1, c2))
			# cnt += 1
		return

	# logic
	# horizontal cut
	for i in range(r1, r2):
		if 2 in arr[i]:
			solution(i+1, r2, c1, c2, n-1)

	for j in range(c1, c2):
		if 2 in cols[j]:
			solution(r1, r2, j+1, c2, n-1)

solution(0, tR, 0, tC, n)

print(len(result))