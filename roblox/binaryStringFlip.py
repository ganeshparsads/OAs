# Binary string of 0's and 1's
# Requests "Count" and "Flip"


ip = "0000101"

arr = list(ip)

requests = ["count", "flip", "flip", "flip", "count"]

n = len(arr)

req_n = len(requests)

count = [0 for i in range(req_n)]

counter = 0

for i in range(n):
	if int(arr[i]) == 1:
		counter += 1

j = 0

for r in requests:
	if r == "count":
		count[j] = counter
		j += 1
	else:

		for k in range(n):
			if int(arr[k]) == 1:
				count[j] = k
				j += 1
				arr[k] = '0'
				counter -= 1
				break
			else:
				arr[k] = '1'
				counter += 1

print(count)
