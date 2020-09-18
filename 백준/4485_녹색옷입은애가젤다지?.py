import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    idx = 0
    while True:
        idx += 1
        N = int(input())
        if N == 0:
            break
        arr = [list(map(int, input().split())) for _ in range(N)] # 비용 정보를 가진 행렬
        INF = int(1e9)
        distance = [[INF]*N for _ in range(N)]
        heap = []

        def dijkstra(r,c):
            heapq.heappush(heap, (arr[r][c], (r,c)))
            distance[r][c] = arr[r][c] # 0이 아님
            while heap:
                cost, node = heapq.heappop(heap)
                for dr, dc in (-1,0),(1,0),(0,-1),(0,1):
                    nr = node[0] + dr
                    nc = node[1] + dc
                    if 0<=nr<N and 0<=nc<N:
                        ncost = cost + arr[nr][nc]
                        if ncost < distance[nr][nc]:
                            distance[nr][nc] = ncost
                            heapq.heappush(heap, (ncost,(nr,nc)))

        dijkstra(0,0)
        print(f'Problem {idx}: '+str(distance[N-1][N-1]))