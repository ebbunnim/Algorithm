import sys
from collections import deque
sys.stdin = open("input.txt", "r")

def melt(y, x):
    cnt=0
    for i in range(4):
        ny=y+D[i][0]
        nx=x+D[i][1]
        if 0<=ny<N and 0<=nx<N:
            if arr[ny][nx]==0:
                cnt+=1
    return cnt

def check(y, x):
    Q.append([y,x])
    visited[y][x]=True
    while Q:
        a=Q.popleft()
        for i in range(4):
            ny=a[0]+D[i][0]
            nx=a[1]+D[i][1]
            if 0<=ny<N and 0<=nx<N and visited[ny][nx]==False and arr_2[ny][nx]!=0:
                visited[ny][nx]=True
                Q.append([ny,nx])


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
arr_2=[[0]*M for _ in range(N)]
for i in range(N):
    arr_2[i] = arr[i][:]
visited=[[False]*M for _ in range(N)]
D = [(1,0), (-1,0), (0,1), (0,-1)]
Q=deque()

ans=0; flag=0

while True:
    for i in range(N):
        for j in range(M):
            if arr[i][j]!=0:
                arr_2[i][j]-=melt(i,j)
