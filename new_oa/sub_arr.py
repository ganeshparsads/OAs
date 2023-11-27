def xor_border_and_center(arr):
    if len(arr) < 2:
        return arr

    left = 0
    right = len(arr) - 1
    result = 's'

    final = False

    while left < right:
        if result == 's':
            result = arr[left] ^ arr[right]
        else:
            if result != arr[left] ^ arr[right]:
                final = False
                break
        left += 1
        right -= 1



    # If there is a single element left at the center, append it without XOR.
    if left == right:
        if result != arr[left]:
            return False

    return final

def get_all_subarrays_efficient(arr):
    subarrays = []
    n = len(arr)
    
    for i in range(n):
        subarray = []
        for j in range(i, n):
            subarray.append(arr[j])
            if len(subarray[:]) >= 3:
                subarrays.append(subarray[:])
    
    return subarrays

arr = [3, 7, 4, 0]

print(get_all_subarrays_efficient(arr))

