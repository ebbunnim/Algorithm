import sys
from collections import deque
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def bfs(s,e):
    if arr[0][0]<s or arr[0][0]>e:
        return

    Q=deque([(0,0)]) # r,c
    vis=[[False]*N for _ in range(N)]
    vis[0][0]=True
    while Q:
        r,c=Q.popleft()
        if r==(N-1) and c==(N-1):
            return True
        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            if 0<=nr<N and 0<=nc<N and not vis[nr][nc]:
                if s<=arr[nr][nc]<=e:
                    vis[nr][nc] = True
                    Q.append((nr,nc))
    return False

def ispath(mid):
    for i in range(200):
        if (i+mid)<=200:
            if bfs(i,i+mid):
                return True
    return False

def bs():
    s,e=0,200
    while s<e:
        mid=(s+e)//2 # 최대-최소
        if ispath(mid):
            e=mid
        else:
            s=mid+1
    return e

if __name__ == '__main__':
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    print(bs())
