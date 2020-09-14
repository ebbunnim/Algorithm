import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    # 방향 : 동쪽, 남쪽, 대각선(동쪽방향)
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    dx = [0, 1, 1]
    dy = [1, 0, 1]
    Q = deque()
    ans = 0
    res = [[0]*N for _ in range(N)]

    def move_by_dir(x, y, dir):
        if dir == 0 :
            nx = x + dx[0]
            ny = y + dy[0]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1:
                Q.append((nx, ny, 0))
            nx = x + dx[2]
            ny = y + dy[2]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and arr[x+1][y]!=1 and arr[x][y+1]!=1:
                Q.append((nx, ny, 2))
        elif dir == 1:
            nx = x + dx[1]
            ny = y + dy[1]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1:
                Q.append((nx, ny, 1))
            nx = x + dx[2]
            ny = y + dy[2]
            if 0 <= nx < N and 0 <= ny < N and arr[nx][ny] != 1 and arr[x+1][y]!=1 and arr[x][y+1]!=1:
                Q.append((nx, ny, 2))
        else:# dir = 2
            if 0 <= x < N and 0 <= y+1 < N and arr[x][y+1] != 1:
                Q.append((x, y+1, 0))
            if 0 <= x+1 < N and 0 <= y < N and arr[x+1][y] != 1:
                Q.append((x+1, y, 1))
            if 0 <= x+1 < N and 0 <= y+1 < N and arr[x][y+1] != 1 and arr[x+1][y] != 1 and arr[x+1][y+1] != 1:
                Q.append((x+1,y+1, 2))


    def bfs(x, y, dir):
        global ans
        Q.append((x,y,dir))
        while Q :
            x, y, dir = Q.popleft()
            if (x,y) == (N-1,N-1):
                ans += 1
                continue
            move_by_dir(x, y, dir)
        return
    bfs(0,1,0) # 앞쪽칸 기준
    print(ans)


