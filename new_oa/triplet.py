def maxTripletSum(arr, n): 
  
    # Initialize the answer 
    ans = -1
  
    for i in range(1, (n - 1)): 
        max1 = 0
        max2 = 0
  
        # find maximum value(less than arr[i]) 
        # from 0 to i-1 
        for j in range(0, i): 
            if (price[j] < price[i]): 
                max1 = max(max1, arr[j]) 
  
        # find maximum value(greater than arr[i]) 
        # from i + 1 to n-1 
        for j in range((i + 1), n): 
            if (price[j] > price[i]): 
                max2 = max(max2, arr[j]) 
  
        # store maximum answer 
                if (max1 > 0 and max2 >0): 
                    ans = max(ans, max1 + arr[i] + max2) 

    return ans 
  
  
# Driver code 

price = [2, 3, 1, 5, 9]
arr = [1, 2, 6, 1, 5]

price = [4, 3, 2, 1]
arr = [4, 3, 2, 1]
n = len(arr) 
print(maxTripletSum(arr, n))
