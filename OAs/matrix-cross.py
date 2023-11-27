from collections import Counter

ip = [[1, 2], [2, 1]]
# ip = [[1,1,1,1], [2,3,1,1], [1,1,1,0], [1,4,1,1]]

n = len(ip)

m = len(ip[0])


rows = []
cols = []

for i in range(m):
	col = []
	for j in range(n):
		col.append(ip[j][i])
	cols.append(col)

countRows = []

# check
for i in ip:	
	counter = Counter(i)
	countRows.append(counter)

countCols = []

for j in cols:
	counter = Counter(j)
	countCols.append(counter)

print(countRows, countCols)


result_row = []
# go through each row
for i in range(n):
	counter = countRows[i]
	keys = list(counter.keys())
	tempRow = []
	for j in range(m):
		if len(counter) > 2:
			tempRow.append((False, -1))
			continue
		elif len(counter) == 1:
			tempRow.append((True, keys[0]))
			continue
		elif len(counter) == 2 and counter[ip[i][j]] == 1:
			idx = keys.index(ip[i][j])
			ele = keys[idx-1]
			tempRow.append((True, ele))
		else:
			tempRow.append((False, -1))
	result_row.append(tempRow)

result_col = []
for k in range(m):
	counter = countCols[k]
	keys = list(counter.keys())
	tempCol = []
	for i in range(n):
		if len(counter) > 2:
			tempCol.append((False, -1))
			continue
		elif len(counter) == 1:
			tempCol.append((True, keys[0]))
			continue
		elif len(counter) == 2 and counter[ip[i][k]] == 1:
			idx = keys.index(ip[i][k])
			ele = keys[idx-1]
			tempCol.append((True, ele))
		else:
			tempCol.append((False, -1))
	result_col.append(tempCol)

cnt = 0
for i in range(n):
	for j in range(m):
		print(i, j)
		if result_row[i][j][0] and result_col[i][j][0] and (result_row[i][j][1] == result_col[i][j][1]):
			cnt += 1

print(cnt)
