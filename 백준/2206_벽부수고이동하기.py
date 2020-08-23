
from collections import deque

def bfs():
    Q.append((0,0,0))
    vis[0][0][0] = True
    D[0][0][0] = 1

    while Q :
        x, y, w = Q.popleft()

        if x == N-1 and y == M-1:
            return D[x][y][w]

        for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M:
                if arr[nx][ny] == 0 and vis[nx][ny][w] == False:
                    D[nx][ny][w] = D[x][y][w] + 1
                    Q.append((nx,ny,w))
                    vis[nx][ny][w] = True

                else: # 벽인 경우
                    if w == 0 and vis[nx][ny][w] == False:
                        D[nx][ny][1] = D[x][y][0] + 1
                        Q.append((nx,ny,1))
                        vis[nx][ny][w] = True
    return -1

if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    Q = deque()
    vis = [[[False]*2 for _ in range(M)] for _ in range(N)]
    D = [[[0]*2 for _ in range(M)] for _ in range(N)]

    print(bfs())
