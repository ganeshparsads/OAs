def getMesStatus(timeStamps, messages, k):
	delivery_sys = {}

	result = []

	for i, val in enumerate(messages):
		if val not in delivery_sys:
			result.append(True)
		else:
			print(delivery_sys)
			if timeStamps[i] - delivery_sys[val] < k:
				result.append(False)
			else:
				result.append(True)

		delivery_sys[val] = timeStamps[i]

	return result


timeStamps = [1, 4, 5, 10, 11, 14]
messages = ["h", "b", "b", "h", "b", "h"]
k = 5
print(getMesStatus(timeStamps, messages, k))
