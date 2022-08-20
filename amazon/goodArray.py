from collections import deque

class Solution:
     def baseNeg2(self, x):
        # res = []
        # while x:
        #     res.append(x & 1)
        #     x = -(x >> 1)
        # end_res = "".join(map(str, res[::-1] or [0]))

        # return end_res
        # # n = len(end_res)
        # # for idx, i in enumerate(end_res.split()):
        # # 	if i == '1':
        # # 		print(i**)
       	res = bin(x).split('0b')[1]
       	n = len(res)
       	arr = []
       	for idx, i in enumerate(res):
       		if i == '1':
       			arr.append(2**(n - idx - 1))

       	arr.reverse()
       	print(arr)

obj = Solution()
obj.baseNeg2(1)
