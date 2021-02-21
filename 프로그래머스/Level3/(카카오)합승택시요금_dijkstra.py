import heapq
import sys

def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n + 1)]
    for f in fares:
        graph[f[0]] += [(f[2], f[1])]
        graph[f[1]] += [(f[2], f[0])]
    INF = sys.maxsize

    # for s, a, b
    def dijkstra(start):
        heap = []
        heapq.heappush(heap, (0, start))
        dist = [INF] * (n + 1)
        dist[start] = 0
        while heap:
            cost, curr = heapq.heappop(heap)
            if dist[curr] < cost:
                continue
            for nxt in graph[curr]:
                ncost = cost + nxt[0]
                if dist[nxt[1]] > ncost:
                    dist[nxt[1]] = ncost
                    heapq.heappush(heap, (ncost, nxt[1]))
        return dist

    ans = INF
    s_table = dijkstra(s)
    a_table = dijkstra(a)
    b_table = dijkstra(b)
    for i in range(1, n + 1):  # 경유지
        ans = min(ans, s_table[i] + a_table[i] + b_table[i])
    return ans