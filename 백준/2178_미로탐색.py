import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    N,M = map(int, input().split())
    graph = [list(map(int,input())) for _ in range(N)]
    vis = [[False]*M for _ in range(N)]
    Q = deque()
    def bfs():
        Q.append((0,0,1))
        vis[0][0] = True
        while Q:
            r,c,d = Q.popleft()
            if r == N-1 and c == M-1:
                return d
            for dr, dc in (-1,0),(1,0),(0,-1),(0,1):
                nr = r + dr
                nc = c + dc
                if 0<=nr<N and 0<=nc<M and vis[nr][nc] == False and graph[nr][nc] == 1:
                    vis[nr][nc] = True
                    Q.append((nr,nc,d+1))
    print(bfs())