# ip = [[3, 1, 3, 1], [1, 1, 1, 4], [3, 1, 2, 2], [3, 3, 3, 4]]
# ip = [[5, 2, 6], [3, 1, 4], [1, 1, 1], [4, 1, 2]]
ip = [[1,2,3,2], [4,1, 4, 5], [5, 3, 4, 4], [1, 2, 2, 1], [1, 5, 2, 1]]

# clearList = deque()
direction=[(0,1),(0,-1),(1,0),(-1,0)]

visited = {}

n = len(ip)

m = len(ip[0])

result = [[ip[j][i] for i in range(m)] for j in range(n)]

for i in range(n):
    for j in range(m):
        curr = ip[i][j]

        cnt = 0
        for dr,dc in direction:
            row=i+dr
            col=j+dc
            if -1<row<n and -1<col<m and ip[row][col]==curr:
                cnt += 1

        if cnt > 1:
            result[i][j] = 0
            for dr,dc in direction:
                row=i+dr
                col=j+dc
                if -1<row<n and -1<col<m and ip[row][col]==curr:
                    result[row][col] = 0

print(result)

for j in range(m):
    new_row = []
    for i in range(n):
        new_row.append(result[i][j])

    print(new_row)

    output=[i for i in new_row if i!=0]

    n_row = []
    for i in range(new_row.count(0)):
        n_row.append(0)

    for i in output:
        n_row.append(i)

    for i in range(n):
        result[i][j] = n_row[i]


print(result)
            