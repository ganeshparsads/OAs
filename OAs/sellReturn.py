from collections import deque

logs = [
	["supply", "item1", "2", "100"],
	["supply", "item2", "3", "60"],
	["sell", "item1", "1"],
	["sell", "item1", "1"],
	["sell", "item2", "2"],
	["return", "item2", "1", "60", "40"],
	["sell", "item2", "1"],
	["sell", "item2", "1"]
]

# logs = [
# 	["supply", "item1", "2", "200"],
# 	["supply", "item2", "3", "100"],
# 	["sell", "item1", "2"],
# 	["sell", "item2", "1"],
# 	["return", "item2", "1", "100", "80"],
# 	["sell", "item2", "3"],
# ]


# sell and return
#{ item1: deque() }
items = {}

# logs = []

result = []

# import pdb
# pdb.set_trace()

for log in logs:
	if log[0] == "supply":

		name = log[1]
		price = int(log[3])
		count = int(log[2])

		if name not in items:
			items[name] = {price: count}
		else:
			# check price
			if price not in items[name]:
				items[log[1]] = {price: count}
			elif price in items[name]:
				items[log[1]][price] += count

	elif log[0] == "sell":
		name = log[1]
		count = int(log[2])
		# print(name, count)

		oSun = 0
		while count != 0:
			if name in items:
				print(items)
				# if name == 'item2':
				# 	import pdb
				# 	pdb.set_trace()
				price_sell = min(list(items[name].keys()))
				if items[name][price_sell] <= count:
					oSun += price_sell * items[name][price_sell]
					count -= items[name][price_sell]
					items[name].pop(price_sell)
				else:
					items[name][price_sell] -= count
					# count = 0
					oSun += price_sell * count
					count = 0
					if items[name][price_sell] == 0:
						items[name].pop(price_sell)

					if not items[name]:
						items.pop(name)

		result.append(oSun)
		if not items[name]:
			items.pop(name)

	elif log[0] == "return":
		name = log[1]
		count = int(log[2])
		price = int(log[4])

		# check price
		if price not in items[name]:
			items[log[1]][price] = count
		elif price in items[name]:
			items[log[1]][price] += count

	# print(items)

print(result)