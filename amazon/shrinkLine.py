
def shrinkLine(arr, n, k):
	# sort(a, a+n)
	arr.sort()
	ans = arr[n-1] - arr[0]

	for i in range(n):
		# print(, arr[i-1])
		print(i)
		mi = min(arr[0]+k, arr[i] - k)
		ma = max(arr[i-1]+k, arr[n-1] - k)

		if ans > ma - mi:
			ans = ma - mi

	print(ans)

shrinkLine([4, 7, -7], 3, 5)
