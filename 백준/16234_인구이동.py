from collections import deque
from copy import deepcopy


def unify(x, y): # bfs
    global is_move
    Q.append((x,y))
    vis[x][y] = True

    sumv = arr[x][y]
    end = -1
    while True:
        flag = 0
        for i in range(len(Q)-1,end,-1):
            x, y = Q[i]
            for dx, dy in (0,-1),(-1,0),(0,1),(1,0):
                nx, ny = x + dx, y + dy
                if 0<=nx<N and 0<=ny<N and vis[nx][ny] == False and L<=abs(arr[x][y]-arr[nx][ny])<=R:
                    vis[nx][ny] = True
                    Q.append((nx,ny))
                    sumv += arr[nx][ny]
                    flag = 1
                    is_move=True
            end = i # 이미 지나왔던 앞의 큐를 탐색하지 않도록
        if flag == 0: # 한번도 큐가 갱신되지 않았다면
            break

    value = sumv//len(Q)
    for i in range(len(Q)-1,-1,-1) :
        x, y = Q[i]
        unions[x][y] = value



if __name__ == '__main__':
    N, L, R  = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    unions = [[0]*N for _ in range(N)]
    ans = 0

    while True:
        is_move = False
        vis = [[False] * N for _ in range(N)] # vis는 배열 자체에서 보는 것이므로 안됨

        for i in range(N):
            for j in range(N):
                if vis[i][j] == False:
                    Q = deque()
                    unify(i,j)
        if is_move==True :
            ans += 1
            arr = deepcopy(unions)
            unions = [[0] * N for _ in range(N)] # 초기화 주의
        else: # 인구가 한번도 이동하지 않았다.
            break

    print(ans)

