import sys
from collections import deque
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def bfs():
    Q=deque([( dst[0][0],dst[0][1],0,0),(dst[0][0],dst[0][1],1,0),(dst[0][0],dst[0][1],2,0),(dst[0][0],dst[0][1],3,0)]) # r,c,d,lv
    vis=[[INF]*W for _ in range(H)]
    vis[dst[0][0]][dst[0][1]] = 0
    while Q:
        r,c,prev_d,lv=Q.popleft()
        for d in range(4):
            nr,nc=r+dr[d],c+dc[d]
            if 0>nr or nr>=H or 0>nc or nc>=W:
                continue
            if arr[nr][nc]=='*':
                continue
            if d==prev_d:
                if lv<=vis[nr][nc]:
                    vis[nr][nc]=lv
                    Q.append((nr,nc,d,lv))
            else:
                if lv+1<=vis[nr][nc]:
                    vis[nr][nc]=lv+1
                    Q.append((nr,nc,d,lv+1))
    return vis[dst[1][0]][dst[1][1]]

if __name__ == '__main__':
    ans=sys.maxsize
    W,H=map(int,input().split())
    arr=[list(input().rstrip()) for _ in range(H)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    dst=[]
    INF=sys.maxsize
    for i in range(H):
        for j in range(W):
            if arr[i][j]=='C':
                dst+=[(i,j)]
    print(bfs())