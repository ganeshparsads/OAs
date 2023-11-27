# # def doXor(arr):
# #     n = len(arr)

# #     middleElement = 'NA'

# #     if n % 2 != 0:
# #         middleElement = arr[n/2]

# #     compare = 'S'

# #     return_val = True

# #     for i in range(n/2):
# #         result = arr[i] ^ arr[n-i-1]

# #         if compare == 'S':
# #             compare = result
# #         else:
# #             if compare != result:
# #                 return_val = False
# #                 break

# #     if middleElement != 'NA' and compare != middleElement:
# #         return False

# #     return return_val


# def xor_of_border(arr):
#     if not arr or len(arr) < 2:
#         return False  # Not enough elements to calculate border XOR

#     n = len(arr)
#     border_xor = 0

#     for i in range(n):
#         if i == 0 or i == n - 1:
#             border_xor ^= arr[i]

#     return border_xor

def are_all_xors_equal(arr):
    if len(arr) < 2:
        return True  # There is only one element or none, so all results are equal

    n = len(arr)
    border_xor = arr[0] ^ arr[-1]

    for i in range(1, n // 2):
        current_xor = arr[i] ^ arr[n - 1 - i]
        if current_xor != border_xor:
            return False

    mid = int(n/2)

    if n %2 != 0 and (arr[0] ^ arr[n - 1]) != arr[mid]:
        return False

    return True


def sublists(arr):
    subarrays = []
    current_subarray = []
    cnt = 0

    for element in arr:
        # Extend the current subarray
        current_subarray.append(element)

        # If the subarray length is 3 or more, add it to the result
        if len(current_subarray) >= 3:
            print(current_subarray[:])
            if are_all_xors_equal(current_subarray[:]):
                cnt += 1
            # subarrays.append(current_subarray[:])

        # If the subarray length exceeds 3, remove the leftmost element
        if len(current_subarray) > 3:
            current_subarray.pop(0)

    return cnt

def get_subarrays(arr):
    subarrays = []
    current_subarray = []

    for element in arr:
        # Extend the current subarray
        current_subarray.append(element)

        # If the subarray length is 3 or more, add it to the result
        if len(current_subarray) >= 3:
            subarrays.append(current_subarray[:])

        # If the subarray length exceeds 3, remove the leftmost element
        if len(current_subarray) > 3:
            current_subarray.pop(0)

    return subarrays

# Example usage:
arr = [1, 2, 3, 4, 5, 6, 7]

# arr = [0, 3, 6, 5]

subarrays = get_subarrays(arr)
print(subarrays)    



# arr = [1, 2, 1]

# print(sublists(arr))
