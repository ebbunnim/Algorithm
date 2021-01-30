import sys
from collections import deque
input=sys.stdin.readline

def bfs(i,j):
    global max_depth
    Q=deque([(i,j,0)])
    vis=[[False]*M for _ in range(N)]
    vis[i][j]=True
    while Q:
        r,c,depth=Q.popleft()
        max_depth=max(max_depth,depth)
        for dr,dc in (-1,0),(1,0),(0,-1),(0,1):
            nr,nc=r+dr,c+dc
            if 0<=nr<N and 0<=nc<M and arr[nr][nc]=='L' and not vis[nr][nc]:
                vis[nr][nc]=True
                Q.append((nr,nc,depth+1))
    return


if __name__ == '__main__':
    N,M=map(int,input().split())
    arr=[list(input().strip()) for _ in range(N)]
    max_depth=0
    starts=[]
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='L':
                starts+=[(i,j)]
    for i,j in starts:
        bfs(i,j)
    print(max_depth)