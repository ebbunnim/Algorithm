import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(1000000)

def dfs(curr,lvl):
    for nxt in graph[curr]:
        if vis[nxt]==False:
            vis[nxt]=True
            lv[nxt]=lvl+1
            dfs(nxt,lvl+1)

def lca(n1,n2):
    while lv[n1]!=lv[n2]:
        if lv[n1]>lv[n2]:
            n1=parent[n1]
        else:
            n2=parent[n2]
    # 동일한 깊이로 왔다면,
    while n1!=n2:
        n1=parent[n1]
        n2=parent[n2]
    return n1

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        N=int(input())
        graph=[[] for _ in range(N+1)]
        parent=[0]*(1+N)
        vis=[False]*(1+N)
        lv=[0]*(1+N)
        for _ in range(N-1):
            A,B=map(int,input().split())
            parent[B]=A
            graph[A]+=[B]
        n1,n2=map(int,input().split())
        root=parent[1:].index(0)+1
        vis[root]=True
        dfs(root,0)
        print(lca(n1,n2))
