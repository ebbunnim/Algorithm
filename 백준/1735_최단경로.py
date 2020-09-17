import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    V, E  = map(int, input().split())
    S = int(input())
    INF = int(1e9)
    graph = [[] for _ in range(V+1)]
    distance = [INF]*(V+1)
    distance[S] = 0
    for _ in range(E):
        s, e, cost = list(map(int, input().split()))
        graph[s].append((e,cost))

    def dijkstra(start):
        heap = []
        heapq.heappush(heap, (0,start))
        while heap:
            cost, node = heapq.heappop(heap)
            if distance[node] < cost:
                continue
            for _node in graph[node]:
                ncost = cost + _node[1]
                if ncost < distance[_node[0]]:
                    distance[_node[0]] = ncost
                    heapq.heappush(heap,(ncost, _node[0]))

    dijkstra(S)
    for i in range(1,V+1):
        if distance[i]!=INF:
            print(distance[i])
        else:
            print('INF')



