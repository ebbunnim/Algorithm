import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline
from collections import deque

def bfs(sr,sc,tr,tc):
    Q=deque([(sr,sc,0)])
    vis=[[False]*w for _ in range(h)]
    vis[sr][sc]=True
    while Q:
        r,c,lv=Q.popleft()
        if r==tr and c==tc:
            return lv
        for d in range(4):
            nr,nc=r+dr[d],c+dc[d]
            if 0<=nr<h and 0<=nc<w and not vis[nr][nc] and arr[nr][nc]!='x':
                vis[nr][nc]=True
                Q.append((nr,nc,lv+1))
    return -1

def dfs(curr,cnt,acc):
    global ans
    if cnt==n:
        ans=min(ans,acc)
        return
    for nxt in range(1,n+1):
        if vis_dfs[nxt]==False:
            vis_dfs[nxt]=True
            if path[curr][nxt]==-1:
                return True
            if dfs(nxt,cnt+1,acc+path[curr][nxt]):
                return True
            vis_dfs[nxt]=False

if __name__ == '__main__':
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    while True:
        w,h=map(int,input().split())
        ans = sys.maxsize
        if w==0 and h==0:
            break
        arr=[list(input().strip()) for _ in range(h)]
        tgts=[]
        for r in range(h):
            for c in range(w):
                if arr[r][c]=='o':
                    sr,sc=r,c
                elif arr[r][c]=='*':
                    tgts.append((r,c))
        n=len(tgts)
        nodes=[(sr,sc)]+tgts
        path=[[0]*(n+1) for _ in range(n+1)]
        for i in range(n+1):
            for j in range(n+1):
                if i==j:
                    continue
                if not path[i][j]:
                    path[i][j]=bfs(nodes[i][0],nodes[i][1],nodes[j][0],nodes[j][1])
                    path[j][i]=path[i][j]
        vis_dfs=[False]*(n+1)
        if dfs(0,0,0):
            print(-1)
        else:
            print(ans)
