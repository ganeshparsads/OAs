
# arr = [1, 2, 1, -4, 5, 10]
arr = [10, 10, 10, 10, 10]

curr = 0

n = len(arr)

result = [0 for i in range(n-2)]

if n < 3:
	# return result
	print(result)

while (curr+2) < len(arr):
	if arr[curr] < arr[curr+1] < arr[curr+2] or arr[curr] > arr[curr+1] > arr[curr+2]:
		result[curr] = 1
	else:
		result[curr] = 0

	curr += 1

print(result)
