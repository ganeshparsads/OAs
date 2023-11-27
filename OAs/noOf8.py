import sys
from collections import Counter

# arr = [0,0,1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,8,8]
arr = [8,8,8,8,8,8,5,5,5,5,5,5,5,5,5,5,5,5]

count = Counter(arr)

if 8 not in count:
	print(0)
	sys.exit(0)

arr_len = len(arr)

noOfTids = arr_len//11

print(min(count[8], noOfTids))
