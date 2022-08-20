
s = "utyrulqaeuouiecodjlmjeaummaoqkexylwaaopnfvlbiiiidyckzfh"
# 

consonets = {}
vowels = ['a', 'e', 'i', 'o', 'u']

for i in range(26):
	char = chr(i + 97)
	if char not in vowels:
		consonets[char] = '1'

result = []

for i in range(len(s)):
	sub = ""
	if s[i] in vowels:
		for j in range(i+1, len(s), 1):
			if s[j] in consonets:
				print(s[i:j+1])
				sub = s[i:j+1]
		if sub:
			result.append(sub)

print(result)
