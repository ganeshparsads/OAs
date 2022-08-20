
# strings = ["aceace", "ceceaa", "abdbdbdbakjkljhkjh"]
strings = ["azbde", "abcher", "acegk"]

# odd
prev = False
# even False
sums = False

for each in strings:
	prev = False
	for i in each:
		if ord(i) % 2:
			curr = True
		else:
			curr = False

		prev = prev and curr

	print(each, prev)
	sums = sums or prev

print(sums)
