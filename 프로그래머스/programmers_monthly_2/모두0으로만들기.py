import sys
sys.setrecursionlimit(1000000)

acc=0
def solution(a, edges):
    global acc
    if sum(a)!=0:
        return -1

    def dfs(src,cnt):
        global acc
        if cnt==n:
            return
        for dst in graph[src]:
            if vis[dst]==False:
                vis[dst]=True
                dfs(dst,cnt+1)
                acc+=abs(a[dst])
                a[src]+=a[dst]

    # make graph
    n=len(a)
    graph=[[] for _ in range(n)]
    check=[0]*n
    for e in edges:
        graph[e[0]]+=[e[1]]
        graph[e[1]]+=[e[0]]
        check[e[0]]+=1
        check[e[1]]+=1
    # leaf 판별, root 노드 지정
    leaves=[i for i in range(n) if check[i]==1]
    root=leaves[0]
    # dfs 탐색
    vis=[False]*n
    vis[root]=True
    dfs(root,0)
    return acc