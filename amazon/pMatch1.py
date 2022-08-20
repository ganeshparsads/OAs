
ip1 = "abcbcdcadbb"
ip2 = "abbc"
p = 3
# ip1 = "zxyzxxyz"
# ip2 = "xxzy"
# p = 1

# ip1 = "acbbca"
# ip2 = "acb"
# p = 2

n = len(ip1)
sort_ip2 = sorted(ip2)
split_ip1 = list(ip1)
m = len(ip2)

count = 0
partition = m * p
reached_end = False

for i in range(n):
	idx = i
	temp = []

	for j in range(m):
		idx = i + j*p
		temp.append(split_ip1[idx])
		print(idx)
		if idx == n-1:
			reached_end = True
	# print(temp)
	# import pdb
	# pdb.set_trace()
	if sorted(temp) == sort_ip2:
		count += 1

	if reached_end:
		break

print("final: ", count)