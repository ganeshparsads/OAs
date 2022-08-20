n = int(input())
p = [input().strip() for _ in range(n)]

fullMask = 2**10-1
cntMask = [0 for _ in range(fullMask+1)]

for s in p:
    mask = 0
    for c in s:
        mask |= 1 << (ord(c) - ord('0'))
    cntMask[mask] += 1

res = 0
for i in range(fullMask+1):
    for j in range(i+1, fullMask+1):
        if i | j == fullMask:
            res += cntMask[i] * cntMask[j]

res += cntMask[fullMask] * (cntMask[fullMask]-1) / 2
print(int(res))