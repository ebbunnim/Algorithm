import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    M,N = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Q = deque()
    vis = [[False]*M for _ in range(N)]
    for r in range(N):
        for c in range(M):
            if arr[r][c] == 1:
                Q.append((r,c,0))
                vis[r][c] = True
    def bfs():
        while Q:
            r, c, d = Q.popleft()
            for dr, dc in (-1, 0), (1, 0), (0, -1), (0, 1):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and vis[nr][nc] == False:
                    Q.append((nr,nc,d+1))
                    vis[nr][nc] = True
        return d
    ans = bfs()
    flag = 0
    # 다 익지 못한다.
    for i in range(N):
        for j in range(M):
            if vis[i][j] == False and arr[i][j]==0:
                flag = 1
                print(-1)
                exit()
    if flag == 0:
        print(ans)


