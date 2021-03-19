import sys
sys.stdin = open('input.txt','r')
from collections import deque
from copy import deepcopy

# 첫번째가 x인 경우는 바로 detect 했어야 됨.
def detect(i,h):
    if not i%2: # 왼쪽에서 날아오는 창
        c=0
        while c<C:
            if arr[h][c]=='.':
                c+=1
                continue
            break
    else: # 오른쪽에서 날아오는 창
        c=C-1
        while 0<=c:
            if arr[h][c]=='.':
                c-=1
                continue
            break
    if 0<=c<C:
        return h,c
    return -1,-1

def hit(i,h): # h에 따라 x를 지우고, x의 사방면을 보면서 최대 4가지 원소가 어떤 클러스터에 속하는지 판별한다.
    # 발견하면 hit함
    r,c=detect(i,h)
    if (r,c)==(-1,-1):
        return
    arr[r][c]='.' # hit
    candidates=[]
    cnt=0
    for d in range(4):
        nr,nc=r+dr[d],c+dc[d]
        if 0<=nr<R and 0<=nc<C and arr[nr][nc]=='x':
            candidates+=[(nr,nc)]
            cnt+=1
    if cnt>=2: # cnt가 하나라고 한다면 모서리부분 꺠진 것이므로 패스
        clustering(candidates)
    return

def clustering(candidates): # candidates 중 떨어질 수 있는 클러스터인지 확인.
    Q=deque()
    vis=[[False]*C for _ in range(R)]
    while candidates:
        r,c=candidates.pop()
        # bfs의 루트가 된다.
        if vis[r][c]: # 이미 다른 클러스터에 속한 것이므로 다시 나눌 필요 없음.
            continue
        Q.append((r,c))
        vis[r][c]=True
        downlist=[(r,c)]
        # 하나의 클러스터
        while Q:
            r,c=Q.popleft()
            for d in range(4):
                nr,nc=r+dr[d],c+dc[d]
                if 0<=nr<R and 0<=nc<C and not vis[nr][nc] and arr[nr][nc]=='x':
                    vis[nr][nc]=True
                    Q.append((nr,nc))
                    downlist.append((nr,nc))
        # 클러스터 만들때마다 down 시킴
        down(downlist)

def down(downlist): # 한 클러스터에 속하는 모든 원소를 우선 1씩 내려본다. 가능하다면 반복
    # 바닥에 닿았는지 검사
    global arr
    downlist.sort(reverse=True) # 바닥과 가장 근접한 애들부터 내리겠다. 그래야 같은 클러스터 x를 안만남
    if downlist[0][0]==R-1: # 이미 바닥에 닿은 클러스터는 바로 종료
        return
    Q=deque(downlist)
    n=len(downlist)
    # 아래 로직이 반복됨
    while True:
        copy_arr=deepcopy(arr)
        for i in range(n):
            r,c=Q.popleft()
            if r+1==R or copy_arr[r+1][c]=='x': # 클러스터는 다른 클러스터나 땅을 만나기 전까지 게속해서 떨어진다.
                return arr
            copy_arr[r][c],copy_arr[r+1][c]='.','x'
            Q.append((r+1,c))
        arr=copy_arr

if __name__ == '__main__':
    R,C=map(int,input().split())
    arr=[list(input()) for _ in range(R)]
    N=int(input())
    heights=list(map(int,input().split()))
    dr=[0,1,0,-1]
    dc=[-1,0,1,0]
    for i in range(N):
        hit(i,R-heights[i]) # 와 이거 헷갈림. (0,0)부터 시작됨에 유의. 층이 반대로 높은 것
    res=''
    for line in arr:
        res+=''.join(line)+'\n'
    print(res)