import heapq

class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        graph = [[] for _ in range(N + 1)]
        for t in times:
            graph[t[0]] += [(t[2], t[1])]
        INF = int(1e9)
        distance = [INF] * (1 + N)

        # start
        distance[K] = 0
        heap = []
        heapq.heappush(heap, (0, K))

        # exec
        while heap:
            cost, curr = heapq.heappop(heap)
            if distance[curr] < cost:
                continue
            for nxt in graph[curr]:
                ncost = nxt[0] + cost
                if ncost < distance[nxt[1]]:
                    distance[nxt[1]] = ncost
                    heapq.heappush(heap, (ncost, nxt[1]))

        ans = max(distance[1:])
        if ans == INF:
            return -1
        else:
            return ans




