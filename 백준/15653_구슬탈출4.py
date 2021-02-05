import sys
from collections import deque
input=sys.stdin.readline

def move(rr,rc,br,bc,d):
    dist_r=dist_b=0
    # red
    while True:
        nrr,nrc=rr+dr[d],rc+dc[d]
        if arr[nrr][nrc]=='#':
            break
        if arr[nrr][nrc]=='O':
            rr,rc=nrr,nrc
            break
        rr,rc=nrr,nrc
        dist_r+=1
    # blue
    while True:
        nbr, nbc = br + dr[d], bc + dc[d]
        if arr[nbr][nbc] == '#':
            break
        if arr[nbr][nbc] == 'O':
            br,bc=nbr,nbc
            break
        br,bc=nbr,nbc
        dist_b += 1
    return (rr,rc,br,bc,dist_r,dist_b)


def bfs():
    while Q:
        rr,rc,br,bc,depth=Q.popleft()
        for i in range(4):
            nrr,nrc,nbr,nbc,dist_r,dist_b=move(rr,rc,br,bc,i)
            # 구멍에 빠지는 경우
            if arr[nrr][nrc] == 'O' and arr[nbr][nbc] == 'O':
                continue
            if arr[nbr][nbc]=='O':
                continue
            if arr[nrr][nrc] == 'O':
                return depth + 1
            # 동일위치 처리
            if nrr == nbr and nrc == nbc:
                if dist_r > dist_b:
                    nrr -= dr[i]
                    nrc -= dc[i]
                else:
                    nbr -= dr[i]
                    nbc -= dc[i]
            if not vis[nrr][nrc][nbr][nbc]:
                vis[nrr][nrc][nbr][nbc]=True
                Q.append([nrr,nrc,nbr,nbc,depth+1])
    return -1


if __name__ == '__main__':
    N,M=map(int,input().split())
    arr=[list(input().strip()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='R':
                rr,rc=i,j
            elif arr[i][j]=='B':
                br,bc=i,j
    dr=[-1,0,1,0]
    dc=[0,1,0,-1]
    Q=deque([(rr,rc,br,bc,0)])
    vis=[[[[False]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
    vis[rr][rc][br][bc]=True
    print(bfs())