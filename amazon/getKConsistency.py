def getkConsistency(stock_prices, k):
	my_result = {}
	result = 0

	i = 0
	j = 0

	max_value = 0

	while j < len(stock_prices):
		if stock_prices[j] in my_result:
			my_result[stock_prices[j]] += 1
		else:
			my_result[stock_prices[j]] = 1

		max_value = max(max_value, my_result[stock_prices[j]])

		if (j - i + 1 - max_value) > k:
			my_result[stock_prices[i]] -= i
			i += 1

		result = max(result, max_value)
		j += 1

	return result

print(getkConsistency([1, -2, 1, 1, 3, 2, 1, -2], 3))
