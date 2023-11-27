n = 2
m = 5
nums = [1, 2, 1, 2, 1]
 
n = 2
m = 4
nums = [1, 1, 2, 1]
 
n = 3
m = 8
nums = [1, 2, 3, 2, 2, 2, 2, 2]
 
n = 4
m = 15
nums = [1, 2, 3, 2, 2, 2, 2, 2, 4, 4, 4, 4, 4, 4, 4]
 
 
maxtime = 0
mintime = 2*m
maxind = -1
minind = -1
task = -1
 
arr = [0]*n
for i in range(m):
    arr[nums[i]-1] += 1
    
for i in range(n):
    if (arr[i] > maxtime):
        maxind = i
        maxtime = arr[i]
    if (arr[i] < mintime):
        minind = i
        mintime = arr[i]
 
 
 
nums = []
for i in range(n):
    nums.append([arr[i], arr[i]])
 
print(nums, maxtime, mintime, maxind, minind)
 
while mintime + 2 < maxtime:
    nums[minind][0] += 2
    nums[maxind][0] -= 1
    nums[maxind][1] -= 1
 
    
 
    maxtime = 0
    mintime = 2*m
    maxind = -1
    minind = -1
    mintask = -1
    maxtask = -1
 
    for i in range(n):
        if (nums[i][0] > maxtime):
            maxind = i
            maxtime = nums[i][0]
        elif (nums[i][0] == maxtime) and (maxtask < nums[i][1]):
            maxtime = nums[i][0]
            maxtask = nums[i][1]
            maxind = i
 
        if (nums[i][0] < mintime):
            minind = i
            mintime = nums[i][0]
        elif (nums[i][0] == mintime) and (mintask < nums[i][1]):
            mintask = nums[i][1]
            
            minind = i
 
    print(nums, maxtime, mintime, maxind, minind)
 
finalans = 0
for i in range(n):
    finalans = max(finalans, nums[i][0])
 
print(finalans)
