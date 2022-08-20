s = "I am using hackerrank to improve programming"
t = "am hackerrank to improve"

output = []

ip = t.split(" ")
i = 0
for word in s.split(" "):
	if i < len(ip) and word == ip[i]:
		i += 1
	else:
		output.append(word)


print(output)
