def findSubArrays(arr,n):
 
    # create a python dict
    hashMap = {}
     
    # create a python list
    # equivalent to ArrayList
    out = []
     
    # tracker for sum of elements
    sum1 = 0
    for i in range(n):
         
        # increment sum by element of array
        sum1 += arr[i]
         
        # if sum is 0, we found a subarray starting
        # from index 0 and ending at index i
        if sum1 == 0:
            out.append((0, i))
        al = []
         
        # If sum already exists in the map
        # there exists at-least one subarray
        # ending at index i with 0 sum
        if sum1 in hashMap:
             
            # map[sum] stores starting index
            # of all subarrays
            al = hashMap.get(sum1)
            for it in range(len(al)):
                out.append((al[it] + 1, i))
        al.append(i)
        hashMap[sum1] = al
    print(out)
    return len(out)

arr = [2, -2, 3, 0, 4, -7]
n = 6

print(findSubArrays(arr, n))
