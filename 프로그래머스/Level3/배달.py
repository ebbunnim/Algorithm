import sys
import heapq

def solution(N, road, K):
    INF = sys.maxsize
    graph = [[] for _ in range(N + 1)]
    for e in road:
        graph[e[0]] += [(e[2], e[1])]
        graph[e[1]] += [(e[2], e[0])]
    dist = [INF] * (1 + N)

    def dijkstra(s):
        heap = []
        heapq.heappush(heap, (0, s))
        dist[s] = 0
        while heap:
            cost, src = heapq.heappop(heap)
            if dist[src] < cost:
                continue
            for dst in graph[src]:
                ncost = cost + dst[0]
                if dist[dst[1]] > ncost:
                    dist[dst[1]] = ncost
                    heapq.heappush(heap, (ncost, dst[1]))
        return dist

    dijkstra(1)
    return sum([1 for e in dist if e <= K])
