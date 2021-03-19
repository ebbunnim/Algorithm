import sys
sys.stdin = open('input.txt','r')
from collections import deque
input=sys.stdin.readline

def set_time():
    global maxv
    Q=deque(waters)
    vis=[[False]*C for _ in range(R)]
    while Q:
        r,c,lv=Q.popleft()
        if lv>maxv:
            maxv=lv
        for d in range(4):
            nr,nc=r+dr[d],c+dc[d]
            if 0<=nr<R and 0<=nc<C and not vis[nr][nc] and arr[nr][nc]=='X':
                Q.append((nr,nc,lv+1))
                vis[nr][nc]=True
                time_of_melt[nr][nc]=lv+1

def bfs(pawn1,pawn2,ubound):
    Q=deque([pawn1])
    vis=[[False]*C for _ in range(R)]
    vis[pawn1[0]][pawn1[1]]=True
    while Q:
        r,c=Q.popleft()
        if (r,c)==pawn2:
            return True
        for d in range(4):
            nr,nc=r+dr[d],c+dc[d]
            if 0<=nr<R and 0<=nc<C and not vis[nr][nc] and time_of_melt[nr][nc]<=ubound:
                vis[nr][nc]=True
                Q.append((nr,nc))
    return False

if __name__ == '__main__':
    R,C=map(int,input().strip().split())
    arr=[list(input().strip()) for _ in range(R)]
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    pawns=[(r,c) for r in range(R) for c in range(C) if arr[r][c]=='L']
    waters=[(r,c,0) for r in range(R) for c in range(C) if arr[r][c]!='X'] # 백조가 있는 공간도 물로 처리하기!
    time_of_melt=[[0]*C for _ in range(R)]
    maxv=0
    set_time()
    # bs
    s,e=0,maxv
    ans=e
    while s<=e:
        target=(s+e)//2
        if bfs(pawns[0],pawns[1],target):
            e=target-1
            ans=min(ans,target)
        else:
            s=target+1
    print(ans)

    # 1. 모든 빙하가 녹기까지 걸리는 시간을 따로 저장한다.
    # 2. 이때, max값이 무엇인지 판별한다. 이분탐색의 구간 max값이 될 것
    # 3. 백조의 위치를 담고, bfs로 이동할 것이다. 이때 이분탐색에서 target값으로 잡은 애를 잡는다.
    # 4. 즉, target보다 작거나 같은 애들 빙하만 지나서 이동할 수 있다.
    # 5. 그렇게 이동할 수 없다면 target값을 늘려. 이동할 수 있다면 target값을 줄여