
string = "000011110000"

if len(string) == 1:
	print(1)

prev = -1
curr = 0
future = curr + 1

count = 0

n = len(string)

string = list(string)


for curr in range(len(string)):
	if string[curr] == "1":
		count += 1
		prev = curr
		future = future + 1		
		continue

	if prev == -1:
		if string[future] == "0" and prev != -1 and string[prev] == "0":
			string[curr] = "1"
			count += 1
			prev = curr
			future = future + 1
			continue

	if future == n:
		if string[prev] == "0":
			string[curr] = "1"
			count += 1
		continue

	if string[prev] == "0" and string[curr] == "0" and string[future] == "0":
		string[curr] = "1"
		count += 1
	prev = curr
	future = future + 1



print(string)
print(count)