import sys
sys.stdin = open('input.txt','r')
from collections import deque
input=sys.stdin.readline

def bfs(target):
    Q=deque([(0,0,arr[0][0],arr[0][0])]) # r,c,minv,maxv
    vis=[[False]*N for _ in range(N)]
    vis[0][0]=True
    res=200
    while Q:
        r,c,minv,maxv=Q.popleft()
        if r==(N-1) and c==(N-1):
            print(minv, maxv)
            res=min(res,maxv-minv)
        for i in range(4):
            nr,nc=r+dr[i],c+dc[i]
            if 0<=nr<N and 0<=nc<N and not vis[nr][nc]:
                nminv=min(minv,arr[nr][nc])
                nmaxv=max(maxv,arr[nr][nc])
                if (nmaxv-nminv)<=target:
                    vis[nr][nc] = True
                    Q.append((nr,nc,nminv,nmaxv))
    return res

def bs():
    s,e=0,200
    while s<e:
        mid=(s+e)//2
        if bfs(mid)<=mid:
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