import sys
sys.stdin = open('/Users/sinjiyoung/PycharmProjects/algorithms_git/algorithm/백준/input.txt','r')

import heapq

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]

    # 전처리
    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                arr[i][j]=1
            else:
                arr[i][j]=0

    # for dijkstra
    INF = int(1e9)
    distance = [[INF]*n for _ in range(n)]
    heap = []

    # exec
    def dijkstra():
        distance[0][0] = 0
        heapq.heappush(heap,(0,0,0))

        while heap:
            cost, r, c = heapq.heappop(heap)
            if distance[r][c] < cost:
                continue
            for dr, dc in (-1,0),(1,0),(0,-1),(0,1):
                nr = r + dr
                nc = c + dc
                if 0<=nr<n and 0<=nc<n:
                    ncost = cost + arr[nr][nc]
                    if ncost < distance[nr][nc]:
                        heapq.heappush(heap,(ncost,nr,nc))
                        distance[nr][nc]=ncost

    dijkstra()
    print(distance[n-1][n-1])