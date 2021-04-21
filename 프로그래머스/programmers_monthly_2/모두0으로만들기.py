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
    for e in edges:
        graph[e[0]]+=[e[1]]
        graph[e[1]]+=[e[0]]
    # dfs 탐색 (root-0번 지정)
    vis=[False]*n
    vis[0]=True
    dfs(0,0)
    return acc