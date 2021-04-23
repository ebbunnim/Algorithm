import sys
from collections import deque
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def can_go(r,c,d):
    return 0<=r<N and 0<=c<N and cache[d][r][c]==False

def move(r,c,d,lv):
    while True:
        nr,nc=r+dr[d],c+dc[d]
        if not can_go(nr,nc,d):
            break
        if arr[nr][nc]=='*':
            break
        elif arr[nr][nc]=='!':
            cache[d][nr][nc]=True
            Q.append((nr,nc,d,lv)) # 거울 설치 안할경우
            for nd in D[d]: # 거울 설치할 경우
                cache[nd][nr][nc]=True
                Q.append((nr,nc,nd,lv+1))
        elif arr[nr][nc]=='#':
            cache[d][nr][nc]=True
            Q.append((nr,nc,d,lv))
        r,c=nr,nc

def bfs(sr,sc):
    global ans
    for d in range(4):
        move(sr,sc,d,0)
    while Q:
        r,c,d,lv=Q.popleft()
        if r==er and c==ec:
            ans=min(ans,lv)
            continue
        move(r,c,d,lv)

    return

if __name__ == '__main__':
    N=int(input())
    ans=sys.maxsize
    arr=[list(input().rstrip()) for _ in range(N)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    D={
        0:(1,3),
        2:(1,3),
        1:(0,2),
        3:(0,2),
    }
    Q=deque()
    cache=[[[False]*N for _ in range(N)] for _ in range(4)]
    tgts=[(i,j) for i in range(N) for j in range(N) if arr[i][j]=='#']
    sr,sc=tgts[0]
    er,ec=tgts[1]
    bfs(sr,sc)
    print(ans)






