def solution(text):

	text = list(text)
	cnt = 0

	if text[0] == "b":
		cnt += 1
	elif text[0] == "c":
		cnt += 2

	for i in range(1, len(text)):
		curr = text[i]
		prev = text[i-1]
		if curr == 'a' and prev == 'a':
			cnt += 2
		elif curr == 'a' and prev == 'b':
			cnt += 1
		elif curr == 'a' and prev == 'c':
			continue
		elif curr == 'b' and prev == 'a':
			continue
		elif curr == 'b' and prev == 'b':
			cnt += 1
		elif curr == 'b' and prev == 'c':
			cnt += 2
		elif curr == 'c' and prev == 'a':
			cnt += 1
		elif curr == 'c' and prev == 'b':
			continue
		elif curr == 'c' and prev == 'c':
			cnt += 2

	return cnt

print(solution("aabcc"))
print(solution("bcaaa"))
print(solution("abcabcabca"))
