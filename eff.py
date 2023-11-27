def max_requests_knapsack(total_bandwidth, bandwidth, request):
    n = len(bandwidth)

    # Initialize a 2D array to store the maximum requests for each bandwidth
    dp = [[0] * (total_bandwidth + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(total_bandwidth + 1):
            # If the current endpoint's bandwidth is greater than the available bandwidth,
            # then the current endpoint cannot be included
            if bandwidth[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Choose the maximum between including and excluding the current endpoint
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - bandwidth[i - 1]] + request[i - 1])

    return dp[n][total_bandwidth]

# Example usage:
total_bandwidth = 500
bandwidth = [200, 100, 350, 50, 100]
request = [270, 142, 450, 124, 189]

result = max_requests_knapsack(total_bandwidth, bandwidth, request)
print("Maximum total number of requests:", result)
