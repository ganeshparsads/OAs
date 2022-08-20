def findMaximumSum(stocks, n, k):
    # Write your code here
    sumstocks=[]
    for i in range(0,len(stocks)-k):
        if(len(set(stocks[i:i+k]))==k):
            sumstocks.append(sum(stocks[i:i+k]))
        
    if len(sumstockprice) == 0:
        return -1
    else:
        return max(sumstockprice)

print(findMaximumSum([1,2,3,7,3,5], 6, 3))
