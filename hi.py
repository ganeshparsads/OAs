def min_max_load_time(burst_time, n, m):

    left = max(burst_time)  # Minimum possible value

    right = sum(burst_time)  # Maximum possible value

    while left <= right:

        mid = (left + right) // 2

        resource_load = 0

        count = 0

        for task_time in burst_time:

            if resource_load + task_time > mid:

                count += 1

                resource_load = 0

            resource_load += task_time

        if count < n:

            right = mid - 1

        else:

            left = mid + 1

    return left  # Minimum possible value of the maximum total load time

# Example

n = 3

m = 6

burst_time = [7,2,]

result = min_max_load_time(burst_time, n, m)

print(result)  # Output will be the minimum possible value

