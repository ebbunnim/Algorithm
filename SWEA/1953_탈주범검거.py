import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, M, R, C, L = map(int,input().split())
        arr = [list(map(int, input().split())) for _ in range(N)]
        # 1. 현재 파이프에서 갈 수 있는 방향
        # 2. 이 방향이 다음 파이프와 맞물릴 수 있는지 파악
        pipes = {
            1 : [(-1,0),(1,0),(0,-1),(0,1)],
            2 : [(-1,0),(1,0)],
            3 : [(0,-1),(0,1)],
            4 : [(-1,0),(0,1)],
            5 : [(1,0),(0,1)],
            6 : [(1,0),(0,-1)],
            7 : [(-1,0),(0,-1)]
        }
        # 큐에 넣어야 할 정보 : 현재의 열과 행, 파이프모양, depth,
        Q = deque()
        vis = [[False]*M for _ in range(N)]
        Q.append((R,C,arr[R][C],1))
        vis[R][C] = True
        ans = 0
        while Q :
            r, c, pipe, depth = Q.popleft()
            if depth == L+1:
                break
            ans += 1
            for dr, dc in pipes[pipe]:
                nr = r + dr
                nc = c + dc
                if 0<=nr<N and 0<=nc<M and vis[nr][nc]==False and arr[nr][nc]!=0:
                    new_pipe_dir = pipes[arr[nr][nc]]
                    if (-dr,-dc) in new_pipe_dir:
                        Q.append((nr,nc,arr[nr][nc],depth+1))
                        vis[nr][nc]= True
        print(f'#{t+1} {ans}')