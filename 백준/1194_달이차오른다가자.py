from collections import deque

def can_go(nx, ny, keys):
    if arr[nx][ny] == '#':
        return False
    if arr[nx][ny] in {'A', 'B', 'C', 'D', 'E', 'F'}:
        if not keys&(1<<(ord(arr[nx][ny].lower())-97)):
            return False
    return True

def bfs():
    Q = deque()
    Q.append([0, sx, sy, 0])
    vis = [[[False]*(1<<6) for _ in range(M)] for _ in range(N)]
    while Q:
        cost, x, y, keys = Q.popleft()
        if arr[x][y] == '1':
            return cost
        for dx, dy in (-1, 0), (1, 0), (0, -1), (0, 1):
            nx = x + dx
            ny = y + dy
            if 0 <= nx < N and 0 <= ny < M and vis[nx][ny][keys]==False and can_go(nx, ny, keys):
                vis[nx][ny][keys] = True
                if arr[nx][ny] in {'a', 'b', 'c', 'd', 'e', 'f'}:
                    nkeys=keys|(1<<(ord(arr[nx][ny])-97))
                    Q.append([cost + 1, nx, ny, nkeys])
                else:
                    Q.append([cost + 1, nx, ny, keys])
    return -1

if __name__ == '__main__':
    N,M  = map(int,input().split())
    arr = [list(input()) for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if arr[i][j]=='0':
                sx,sy=i,j
                break
    print(bfs())