import ast
import itertools


data = [
	["1", "+", "3", "-", "2"],
	["-", "2", "+", "3", "+"],
	["1", "-", "4", "-", "4"],
	["+", "2", "-", "7", "+"],
	["2", "+", "5", "+", "9"],
	["+", "1", "+", "8", "-"],
	["2", "-", "0", "-", "2"]
]

def subsets(expr):
	result = []
	for i in range(0, len(expr) + 1):
		for subset in itertools.combinations(expr, i):
			result.append(list(subset))

	return result

def valid_expression(expr_str):
	leng = len(expr_str)
	isdigit = True
	for i in expr_str:
		if bool(isdigit) != bool(i.isdigit()):
			return False

		if isdigit and i.isdigit():
			isdigit = False
			continue

		isdigit = True

	return True

n = len(data)
m = len(data[0])
max_value = -1


# digit extraction
for i in range(n):
	for j in range(m):
		if data[i][j].isdigit():
			max_value = max(max_value, int(data[i][j]))


column_wise = []
for j in range(m):
	column = []
	for i in range(n):
		column.append(data[i][j])

	column_wise.append(column)


		
for i in range(n):
	rows = subsets(data[i])
	for sub in rows:		
		if not valid_expression(sub):
			continue
		if len(sub) < 3 and not valid_expression(sub):
			continue
		try:
			expr = ''.join(sub)
			ast.parse(expr)
			val = eval(expr)
			max_value = max(val, max_value)
		except SyntaxError:
			continue

for j in range(len(column_wise)):
	cols = subsets(column_wise[j])
	for sub in cols:
		if not valid_expression(sub):
			continue
		if len(sub) < 3 and not valid_expression(sub):
			continue
		try:
			expr = ''.join(sub)
			ast.parse(expr)
			val = eval(expr)
			max_value = max(val, max_value)
		except SyntaxError:
			continue

print(max_value)