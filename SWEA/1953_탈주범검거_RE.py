import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    T = int(input())
    for t in range(T):
        N, M, R, C, L = map(int,input().split()) # 세로,가로, 현재 행,열, 소요시간
        arr = [list(map(int, input().split())) for _ in range(N)]
        vis = [[False]*M for _ in range(N)]
        area = 1

        pipes = {
            1: [[-1,0],[1,0],[0,-1],[0,1]],
            2: [[-1,0],[1,0]],
            3: [[0,-1],[0,1]],
            4: [[-1,0],[0,1]],
            5: [[1,0],[0,1]],
            6: [[1,0],[0,-1]],
            7: [[-1,0],[0,-1]]
        }

        Q = deque()
        Q.append([(R,C),1])
        vis[R][C]=True

        while Q:
            idx,depth=Q.popleft()
            if depth==L:
                break
            r, c = idx[0],idx[1]
            for dr,dc in pipes[arr[r][c]]:
                nr = r+dr
                nc = c+dc
                if 0<=nr<N and 0<=nc<M and vis[nr][nc]==False and arr[nr][nc]!=0 and ([-dr,-dc] in pipes[arr[nr][nc]]) :
                    vis[nr][nc]=True
                    Q.append(([nr,nc],depth+1))
                    area += 1

        print(f'#{t+1} {area}')
