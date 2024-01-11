from collections import defaultdict    

def solve(n,edges):
    adjList = defaultdict(set)
    for u,v in edges:
        adjList[u].add(v)
        adjList[v].add(u)

    sub = [0]*n
    diam = 0

    def dfs1(root,par):
        nonlocal diam,sub
        dist1,dist2 = -1,-1
        for child in adjList[root]-{par}:
            curr = dfs1(child,root)
            if curr>=dist1 :
                dist1,dist2 = curr,dist1
            elif curr>=dist2 :
                dist2 = curr
        diam = max(diam,dist1+dist2+2)
        sub[root] = dist1+1
        return sub[root]

    res = []
    def dfs2(root,par,dist):  
        nonlocal res,diam
        if dist == diam :
            res.append(root)
        for child in adjList[root]-{par}:
            dfs2(child,root,dist+1)
        
    for node in adjList:
        if len(adjList[node]) == 1 :
            root = node
            break
    dfs1(root,-1)
    
    mid = diam//2
    if diam%2 :
        root1,root2  = sub.index(mid), sub.index(mid+1)
        dfs2(root1,root2,mid+1)
        dfs2(root2,root1,mid+1)
    else:
        root1 = sub.index(mid)
        dfs2(root1,-1,mid)

    return res


print(solve(9,[(1,2),(2,3),(3,4),(3,5),(1,6),(1,7)]))
# print(solve(6,[(1,0),(2,0),(3,0),(4,0),(5,0)]))
# print(solve(6,[(0,1),(2,1),(1,3),(3,4),(3,5)]))
# print(solve(9,[(0,1),(2,1),(1,3),(3,4),(3,5),(3,6),(6,7),(6,8)]))
