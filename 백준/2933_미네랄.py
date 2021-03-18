import sys
sys.stdin = open('input.txt','r')
from collections import deque

def detect(i,h):
    if not i%2: # 짝수일 경우에는
        c=0
        while True:
            if c+1<C and arr[h][c+1]=='.':
                c+=1
            else:
                if c+1>=C:
                    return -1,-1
                return h,c+1
    else:
        c=C-1
        while True:
            if 0<=c-1 and arr[h][c-1]=='.':
                c-=1
            else:
                if c-1<0:
                    return -1,-1
                return h,c-1

def hit(i,h): # h에 따라 x를 지우고, x의 사방면을 보면서 최대 4가지 원소가 어떤 클러스터에 속하는지 판별한다.
    # 발견하면 히트임
    r,c=detect(i,h)
    if (r,c)==(-1,-1):
        return
    arr[r][c]='.'
    candidates=[]
    cnt=0
    for d in range(4):
        nr,nc=r+dr[d],c+dc[d]
        if 0<=nr<R and 0<=nc<C and arr[nr][nc]!='.':
            candidates+=[(nr,nc)]
            cnt+=1
    if cnt>=2:
        clustering(candidates)
    return

def clustering(candidates): # 클러스터 번호를 새겨가면서 같은 클로스터인지 아닌지를 판별한다.
    Q=deque()
    vis=[[False]*C for _ in range(R)]
    while candidates:
        r,c=candidates.pop()
        # bfs의 루트가 된다.
        # 번호를 나누는 작업이 너무 번거로움. 현재 위치에서 쪼개져야 하므로
        if vis[r][c]: # 클러스터를 나눌 필요가 없음
            continue
        Q.append((r,c))
        vis[r][c]=True
        downlist=[(r,c)]
        # 하나의 클러스터
        while Q:
            r,c=Q.popleft()
            for d in range(4):
                nr,nc=r+dr[d],c+dc[d]
                if 0<=nr<R and 0<=nc<C and not vis[nr][nc] and arr[nr][nc]!='.':
                    vis[nr][nc]=True
                    Q.append((nr,nc))
                    downlist.append((nr,nc))
        down(vis,downlist)

def down(vis,downlist): # 한 클러스터에 속하는 모든 원소를 우선 1씩 내려본다. 다른 클러스터 번호로 넘어가는 것이 아니면 계속 반복한다.
    # 바닥에 닿았는지 검사
    downlist.sort(reverse=True)
    # Q=deque(downlist)
    # n=len(downlist)
    # if Q[0][0]==R-1:
    #     return
    # while True: #  1씩 내려볼 것임. 바닥이거나 다른것에 다으면 stop
    #     flag=0
    #     for i in range(n): # 큐 한번 순회
    #         r,c=Q[i]
    #         if r==R: # 다음 번에 이미 바닥에 닿아있으면(바닥에 닿게 이미 움직여놓은 상태)
    #             flag=1
    #             break
    #         Q.append((r+1,c))
    #     # downilst 정상적으로 가져왔다면, 현재도 바닥에 있는애부터 내릴 상태임.
    #     if flag==1:
    #         break
    #     for i in range(n):
    #         r,c=Q.popleft()
    #         arr[r+1][c],arr[r][c]='x','.'
    #         # vis[r+1][c],vis[r][c]=True,False
    #     if flag==1:
    #         break

if __name__ == '__main__':
    R,C=map(int,input().split())
    arr=[list(input()) for _ in range(R)]
    N=int(input())
    heights=list(map(int,input().split()))
    dr=[0,1,0,-1]
    dc=[-1,0,1,0]
    for i in range(N):
        hit(i,R-heights[i]) # 와 이거 헷갈림. (0,0)부터 시작되어야 함.
        print(*arr,sep='\n')
        print()
    res=''
    for line in arr:
        res+=''.join(line)+'\n'
    print(res)