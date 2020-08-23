from collections import deque

def water():
    L = len(waters)
    for _ in range(L):
        x, y = waters.popleft()
        for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and vis[nx][ny] == False:
                if arr[nx][ny] == '.':
                    vis[nx][ny] = True
                    waters.append((nx,ny))
    return


def bfs():

    Q.append(start)
    vis[start[0]][start[1]] = True

    while Q :
        water() # 물이 먼저 퍼짐
        for _ in range(len(Q)): # 한 depth의 큐 명시
            x, y, d = Q.popleft()

            if (x, y) == end:
                return d


            for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
                nx = x + dx
                ny = y + dy
                nd = d + 1
                if 0<=nx<N and 0<=ny<M and vis[nx][ny] == False:
                    Q.append((nx,ny,nd))
                    vis[nx][ny] = True

    return 'KAKTUS'

if __name__ == '__main__':
    N, M= map(int, input().split())
    arr = [list(input()) for _ in range(N)]
    waters = deque()
    Q = deque()
    vis = [[False]*M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if arr[i][j] == '*':
                waters.append((i,j))
                vis[i][j] = True
            elif arr[i][j] == 'X':
                vis[i][j] = True
            elif arr[i][j] == 'S':
                start = (i,j,0)
            elif arr[i][j] == 'D':
                end = (i,j)

    print(bfs())
