# ip = "aabcdea"
# op = 3

ip = "alabama"
op = 4

count = 0
temp = set()

for i in list(ip):
	if i not in temp:
		temp.add(i)
	else:
		count += 1
		temp = set(i)

if count + 1 == op:
	print(count+1)

else:
	print("fucked up!!!")
