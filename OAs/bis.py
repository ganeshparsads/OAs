from bisect import bisect_left, bisect_right
 
# Function to count pairs whose
# sum lies over the range [L, R]
def countPairSum(arr, L, R, N):
     
    # Sort the given array
    arr.sort()
 
    right = N - 1
    count = 0
 
    # Iterate until right > 0
    while (right > 0):
 
        # Starting index of element
        # whose sum with arr[right] >= L
        it1 = bisect_left(arr, L - arr[right])
 
        start = it1
 
        # Ending index of element
        # whose sum with arr[right] <= R
        it2 = bisect_right(arr, R - arr[right])
 
        it2 -= 1
        end = it2
 
        # Update the value of end
        end = min(end, right - 1)
 
        # Add the count of elements
        # to the variable count
        if (end - start >= 0):
            count += (end - start + 1)
 
        right -= 1
 
    # Return the value of count
    return count
 
# Driver Code
if __name__ == '__main__':
     
    arr = [ 2, 3, 4, 5 ]
    L = 5
    R = 7
    N = len(arr)
     
    print(countPairSum(arr, L, R, N))