

def minKeyPress(s):
	cnt = [0 for i in range(26)]

	for char in s:
		cnt[ord(char) - 97] += 1


	sorted(cnt)

	num = 0
	res = 0

	for i in range(25, -1, -1):
		if num < 9:
			res += cnt[i]
		elif num < 18:
			res += cnt[i] * 2
		elif num < 27:
			res += cnt[i] * 3

		num += 1

	return res


print(minKeyPress("abcghdiefjoba"))
