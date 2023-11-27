

ip = [1, 2, 1]
i = 0

def Candies(arr):
    n = len(arr)
    if n<2:
        return 0
    ans=0
    i=0
    j=n-1
    Alice=arr[0]
    Bob=arr[n-1]
    while(i<j):
        if(Alice == Bob):
            ans=i+1+n-j
            i+=1
            j-=1
            Alice+=arr[i]
            Bob+=arr[j]
        elif Alice>Bob:
            j-=1
            Bob+=arr[j]
        else:
            i+=1
            Alice+=arr[i]
    return ans

print(Candies(ip))

# t=int(input())
# for i in range(t):
#     n=int(input())
#     arr=list(map(int,input().split()))
#     print(Candies(arr,n))

