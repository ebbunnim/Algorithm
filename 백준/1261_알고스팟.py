import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    M, N = map(int, input().split()) # 가로, 세로
    arr = [list(map(int,input())) for _ in range(N)]
    INF = int(1e9)
    distance = [[INF]*M for _ in range(N)]
    distance[0][0] = 0
    heap = []

    def dijkstra(x,y):
        heapq.heappush(heap, (0,(x,y)))
        while heap:
            cost, node = heapq.heappop(heap)
            if distance[node[0]][node[1]]<cost:
                continue
            for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
                nx = node[0] + dx
                ny = node[1] + dy
                if 0<=nx<N and 0<=ny<M:
                    ncost = cost + arr[nx][ny]
                    if ncost < distance[nx][ny]:
                        heapq.heappush(heap, (ncost,(nx,ny)))
                        distance[nx][ny] = ncost
    dijkstra(0,0)
    print(distance[N-1][M-1])

