def maximumEfficiency(memory):
    n = len(memory)
    mod = 10**9 + 7

    def calculate_efficiency(arr):
        return sum((i + 1) * arr[i] for i in range(n)) % mod

    max_efficiency = calculate_efficiency(memory)

    for idx in range(1, n // 2 + 1):
        for i in range(n - 2 * idx + 1):
            j = i + 2 * idx - 1

            # Swap the data within the distance specified by idx
            temp = memory[i:j+1]
            temp.sort()

            # Reconstruct the memory array after the swap
            new_memory = memory[:i] + temp + memory[j+1:]

            max_efficiency = max(max_efficiency, calculate_efficiency(new_memory))

    return max_efficiency


# Example usage:
memory = [5, 1, 4, 2, 4, 1, 2, 3]
result = maximumEfficiency(memory)
print(result)
