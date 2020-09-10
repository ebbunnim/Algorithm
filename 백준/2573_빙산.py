import sys
sys.stdin = open('input.txt','r')

from copy import deepcopy
from collections import deque

if __name__ == '__main__':
    N,M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # 녹이는 함수
    # 덩어리를 확인하는 함수
    def melt(x,y):
        cnt = 0
        for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
            if 0<=x+dx<N and 0<=y+dy<M and arr[x+dx][y+dy] == 0:
                cnt += 1
        copy_arr[x][y]-=cnt
        if copy_arr[x][y] <0:
            copy_arr[x][y] = 0
        return copy_arr

    def find_group(x, y):#dfs 돌려주
        Q = deque()
        Q.append((x,y))
        while Q :
            x, y = Q.popleft()
            for dx, dy in (-1,0),(1,0),(0,-1),(0,1):
                nx, ny = x+dx, y+dy
                if 0<=nx<N and 0<=ny<M and arr[nx][ny]!=0 and vis[nx][ny] == False:
                    vis[nx][ny] = True
                    Q.append((nx,ny))
        return
    ans = 0
    while True:
        ans += 1 # 1년 흘렀다.
        copy_arr = deepcopy(arr)
        for i in range(N):
            for j in range(M):
                melt(i,j)
        arr = deepcopy(copy_arr)

        vis = [[False]*M for _ in range(N)]
        _cnt = 0
        for i in range(N):
            for j in range(M):
                if arr[i][j]!=0 and vis[i][j] == False:
                    find_group(i, j)
                    _cnt += 1
        if _cnt >= 2:
            flag = ans
            break
        if _cnt == 0:
            flag = 0
            break

    print(flag)