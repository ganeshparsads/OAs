def travelAroundTheWorld(a, b, c):
    a = [min(i,c) for i in a]
    # if max(b) > c:
    #     return 0
    min_req, max_reached, remaining_cap,Min_req, Max_reached, Remaining_cap= ([0]*(len(a)+1) for _ in range(6))
    for i in range(1,len(a)):
        if b[i-1] > a[i-1]+remaining_cap[i-1]:
            if c-max_reached[i-1] < b[i-1]-remaining_cap[i-1]-a[i-1]:
                return 0
            min_req[i] = min_req[i-1] + b[i-1]-remaining_cap[i-1]-a[i-1]
            remaining_cap[i] = 0
            max_reached[i] = max(max_reached[i-1]+b[i-1]-remaining_cap[i-1]-a[i-1],b[i-1])
        else:
            min_req[i] = min_req[i-1]
            remaining_cap[i] = min(remaining_cap[i-1]+a[i-1], c) - b[i-1]
            max_reached[i] = max(max_reached[i-1],min(remaining_cap[i-1]+a[i-1], c))
    for i in range(len(a)-1,0,-1):
        if Min_req[i+1] + b[i] > c:
            return 0
        if b[i] > a[i]:
            Min_req[i] = Min_req[i+1] + b[i]-a[i]
            Remaining_cap[i] = Remaining_cap[i+1]
            Max_reached[i] = max(Max_reached[i+1], a[i]+Min_req[i])
        elif a[i]-b[i]>Min_req[i+1]:
            Min_req[i] = 0
            Remaining_cap[i] = Remaining_cap[i+1] + min(c-Max_reached[i+1], a[i]-b[i]-Min_req[i+1])
            Max_reached[i] = max(a[i], min(c, Max_reached[i+1]+a[i]-b[i]-Min_req[i+1]))
        else:
            Min_req[i] = Min_req[i+1] + b[i]-a[i]
            Remaining_cap[i] = Remaining_cap[i+1]
            Max_reached[i] = max(Max_reached[i+1], Min_req[i]+a[i])
    print(min_req, max_reached, remaining_cap,Min_req, Max_reached, Remaining_cap)
    ans = 0
    if min_req[1] == 0 and remaining_cap[1] >= Min_req[1]:
        ans = 1
    for i in range(1,len(a)):
        if Min_req[i] == 0 and Remaining_cap[i] >= min_req[i]:
            ans += 1
    return ans

print(travelAroundTheWorld([2,3,4], [3,1,1], 2))
