import sys
from collections import deque
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def bfs():
    Q=deque([(s[0],s[1],0,1)])
    vis[0][s[0]][s[1]]=True
    while Q:
        r,c,lv,key=Q.popleft()
        if arr[r][c]=='1':
            return lv
        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            nkey = key
            if nr<0 or nr>=N or nc<0 or nc>=M or arr[nr][nc]=='#':
                continue
            if arr[nr][nc] in ('a','b','c','d','e','f'):
                nkey=key|(1<<(ord(arr[nr][nc])-96))
            elif arr[nr][nc] in ('A','B','C','D','E','F'):
                if not key&(1<<(ord(arr[nr][nc])-64)):
                    continue
            if vis[nkey][nr][nc] == False:
                vis[nkey][nr][nc] = True
                Q.append((nr,nc,lv+1,nkey))
    return -1


if __name__ == '__main__':
    N,M=map(int,input().split())
    arr=[list(input()) for _ in range(N)]
    vis=[[[False]*M for _ in range(N)] for _ in range(1<<7)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    flag=0
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='0':
                s=(i,j)
                flag=1
                break
        if flag==1:
            break
    print(bfs())