ip1 = "acaccaa"
ip2 = "aac"

# ip1 = "acbbca"
# ip2 = "acb"

n = len(ip1)
print(n)
sort_ip2 = sorted(ip2)
split_ip1 = list(ip1)
m = len(ip2)
p = 2
count = 0
partition = m * p

for i in range(n):
	if partition + i - 1 > n:
		break

	idx = i
	temp = []
	for j in range(m):
		temp.append(split_ip1[idx])
		idx += p
	print(i, temp)
	if sorted(temp) == sort_ip2:
		count += 1

print(count)