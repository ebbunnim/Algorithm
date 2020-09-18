import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    V = int(input())
    E = int(input())
    graph = [[] for _ in range(1+V)]
    for _ in range(E):
        s, e, c = map(int, input().split())
        graph[s].append((c,e))
    Start, End = map(int, input().split())
    INF = int(1e9)
    distance = [INF]*(1+V)
    distance[Start] = 0

    def dijkstra(start):
        heap = []
        heapq.heappush(heap, (0,start))
        while heap :
            cost, node = heapq.heappop(heap)
            if distance[node] < cost:
                continue
            for _node in graph[node]:
                ncost = cost + _node[0]
                if ncost < distance[_node[1]]:
                    distance[_node[1]] = ncost
                    heapq.heappush(heap,(ncost, _node[1]))
    dijkstra(Start)
    print(distance[End])


