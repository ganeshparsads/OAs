import sys
import copy


def minTotalCost(price):

    min_sum = 1000000

    for idx, val in enumerate(price):
        new_array = copy.deepcopy(price)

        new_array[idx] = new_array[idx] // 2

        prefix_sum = []

        print(new_array)

        for i in range(1, len(new_array)):
            prefix_sum.append(abs(new_array[i] - new_array[i-1]))

        min_sum = min(min_sum, sum(prefix_sum))

    return min_sum

# price = [22, 18, 57]

price = [2, 2, 2]

print(minTotalCost(price))
