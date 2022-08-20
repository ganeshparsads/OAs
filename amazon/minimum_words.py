

s = "Python it programming Python call hello"
t = "programming Python call"

output = "Python it hello"

result = []

for i in t.split(' '):
	fragments = s.split(i)
	if fragments[0].strip():
		result += fragments[0].split(' ')
	s = fragments[1]

print result
