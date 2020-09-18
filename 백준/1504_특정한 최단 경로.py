import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for _ in range(1+V)]
    for _ in range(E):
        s, e, c = map(int,input().split())
        graph[s].append((c,e))
        graph[e].append((c,s))
    E1, E2 = map(int, input().split())
    INF = int(1e9)
    def dijkstra(start):
        distance = [INF]*(1+V)
        distance[start] = 0
        heap = []
        heapq.heappush(heap,(0,start))
        while heap:
            cost, node = heapq.heappop(heap)
            if distance[node] < cost:
                continue
            for _node in graph[node]:
                ncost = cost + _node[0]
                if ncost < distance[_node[1]]:
                    distance[_node[1]] = ncost
                    heapq.heappush(heap,(ncost, _node[1]))
        return distance
    ans1 = dijkstra(1)[E1] + dijkstra(E1)[E2] + dijkstra(E2)[V]
    ans2 = dijkstra(1)[E2] + dijkstra(E2)[E1] + dijkstra(E1)[V]
    ans = min(ans1, ans2)
    if ans >= INF:
        print(-1)
    else:
        print(ans)