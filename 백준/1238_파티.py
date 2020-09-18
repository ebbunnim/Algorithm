import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    V, E, X = map(int, input().split())
    graph = [[] for _ in range(1+V)]
    for _ in range(E):
        s, e, c = map(int, input().split())
        graph[s].append((c,e))
    INF = int(1e9)

    def dijkstra(start):
        heap = []
        distance = [INF] * (1 + V)
        distance[start]=0
        heapq.heappush(heap, (0,start))
        while heap:
            cost, node = heapq.heappop(heap)
            if distance[node] < cost:
                continue
            for _node in graph[node]:
                ncost = cost + _node[0]
                if ncost < distance[_node[1]]:
                    distance[_node[1]]=ncost
                    heapq.heappush(heap,(ncost,_node[1]))
        return distance
    ans = [0]*(1+V)
    X_to_home = dijkstra(X)
    for i in range(1,V+1):
        ans[i] = (X_to_home[i] + dijkstra(i)[X])
    print(max(ans))
