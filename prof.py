def min_time_to_complete_tasks(n, m, data):
    proficient_users = [0] * n  # Initialize an array to store the count of tasks for each user

    # Count the number of tasks for each user
    for task in data:
        proficient_users[task - 1] += 1

    left, right = 1, m  # Initialize left and right pointers for binary search

    while left < right:
        mid = (left + right) // 2
        max_time = max(mid, max(proficient_users))  # Ensure at least 'mid' tasks for proficient users

        # Check if it's possible to distribute tasks among users such that no one takes more than 'mid' time
        can_distribute = all(task <= mid for task in proficient_users)

        if can_distribute:
            right = max_time
        else:
            left = max_time + 1


    print(max_time)

    return left

# Example usage:
n = 3
m = 6
data = [1, 2, 3, 2, 2, 2]

min_time = min_time_to_complete_tasks(n, m, data)
print("Minimum time to complete tasks:", min_time)
