import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def dfs(curr,stack):
    vis[curr]=True
    stack.append(curr)
    nxt=Nlist[curr]
    if not vis[nxt]:
        if not dfs(nxt,stack):
            return
    elif vis[nxt] and (nxt in stack):
        while stack:
            x=stack.pop()
            cycle[x]=True
            if x==nxt:
                break

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        Nlist=[0]+list(map(int,input().split()))
        vis=[False]*(1+N)
        cycle=[False]*(1+N)
        for i in range(1,N+1):
            dfs(i,[])
        print(N-sum(cycle))