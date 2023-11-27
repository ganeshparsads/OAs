class Solution:
	def solution(A):
		result = 0
		hMap = {}

		for idx, val in enumerate(A):
			if i not in hMap:
				hMap[val] = i
			else:
				result = max(result, idx - hMap[val])

		return result
