

# a = [1, 1, 2, 2, 3]
# b = 1

a = [2, 8, 4, 6, 5]
b = 2

a = sorted(a)


for i in a:
	if b == i:
		b += i

print(b)
