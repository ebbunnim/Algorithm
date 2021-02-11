import sys
sys.stdin = open('input.txt','r')

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
    N = int(input())
    Nlist=[0]+[int(input()) for _ in range(N)]
    cycle=[False]*(1+N)
    vis=[False]*(1+N)
    for i in range(1,1+N):
        dfs(i,[])
    print(sum(cycle))
    for i in range(1,N+1):
        if cycle[i]:
            print(i)
