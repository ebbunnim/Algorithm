from collections import deque

def same(x,y,nx,ny):
    if arr[x][y] == arr[nx][ny]:
        return True


def bfs(start_row, start_col):
    global ans

    ans += 1
    Q.append((start_row,start_col))

    while Q :
        x, y = Q.popleft()
        for a,b in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx = x + a
            ny = y + b

            if 0<=nx<N and 0<=ny<N and vis[nx][ny] == False:
                if same(x,y,nx,ny):
                    vis[nx][ny] = True
                    Q.append((nx, ny))


if __name__ == '__main__':
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    vis = [[False]*N for _ in range(N)]
    ans = 0

    Q = deque()

    for i in range(N):
        for j in range(N):
            if vis[i][j] == False:
                vis[i][j] = True
                bfs(i, j)
    print(ans)
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'G':
                arr[i][j] = 'R'
    ans = 0
    vis = [[False]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if vis[i][j] == False:
                vis[i][j] = True
                bfs(i, j)
    print(ans)