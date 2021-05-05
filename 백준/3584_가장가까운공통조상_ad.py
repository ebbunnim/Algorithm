import sys
from math import ceil, log2
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(1000000)

def dfs(curr,lvl):
    for nxt in graph[curr]:
        if vis[nxt]==False:
            vis[nxt]=True
            lv[nxt]=lvl+1
            dfs(nxt,lvl+1)

def set_parent(root):
    dfs(root,0)
    for i in range(1,H):
        for j in range(1,N+1):
            parent[j][i]=parent[parent[j][i-1]][i-1]
    return

def lca(n1,n2):
    # 레벨을 동일하게 맞추자
    if lv[n1]>lv[n2]:
        n1, n2 = n2, n1
    for i in range(H-1,-1,-1): # 지수승으로 올려보낸다.
        if lv[n2]-lv[n1]>=(1<<i):
            n2 = parent[n2][i]
    if n1==n2:
        return n1
    # 가장 가까운 공통 부모 찾기
    for i in range(H-1,-1,-1):
        if parent[n1][i]!=parent[n2][i]:
            n1 = parent[n1][i]
            n2 = parent[n2][i]
    return parent[n1][0]

if __name__=="__main__":
    T=int(input())
    for _ in range(T):
        N=int(input())
        H=int(ceil(log2(N))) # 트리의 높이(레벨 : 0,1,...,H)
        graph=[[] for _ in range(N+1)]
        parent=[[0]*H for _ in range(1+N)] # row : 노드번호, col : 2승씩 0,1,2...번쨰로 건너뛰어서 만난 부모 찾도록 제어
        vis=[False]*(1+N)
        lv=[0]*(1+N)
        for _ in range(N-1):
            A,B=map(int,input().split())
            graph[A]+=[B]
            parent[B][0]=A
            # parent 정보를 어떻게?
        n1,n2=map(int,input().split())
        for i in range(1,N+1):
            if parent[i][0]==0:
                root=i
                break
        set_parent(root)
        print(lca(n1,n2))
