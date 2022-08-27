import heapq
from collections import deque

class Solution:
	def lighting(self, intervals, points):
		intervals.sort()
		dq = deque(intervals)
		minHeap = []
		dict_a = {}

		old_points = list(points)

		points.sort()

		for i in points:
			# popleft from deque and push to the heap
			while dq and ((dq[0][0] <= i and i >= dq[0][1]) \
					or (dq[0][0] <= i and i <= dq[0][1])):
				start, end = dq.popleft()
				if start <= i and i <= end:
					heapq.heappush(minHeap, end)

			# pop from heap unneccessary elements
			while minHeap and minHeap[0] < i:
				heapq.heappop(minHeap)

			dict_a[i] = len(minHeap)

		result = []
		for i in old_points:
			result.append(dict_a[i])

		return result

obj = Solution()

intervals = [[2, 4], [2, 7], [2, 9], [2, 11], [2, 12]]

points = [37, 7, 5, 14, 33, 40, 7]

print(obj.lighting(intervals, points))
