import heapq


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        # src -> dst
        # k 개의 경유개 (중간에 거치는 애) 제약사항 - 각 노드로 가는 최단거리 테이블 삭제. k 조건 안맞으면 최소로 풀지 못하므로
        graph = [[] for _ in range(n)]
        for edge in flights:
            graph[edge[0]] += [(edge[2], edge[1])]

        # start
        heap = []
        heapq.heappush(heap, (0, src, 0))
        ans = -1

        # exec
        while heap:
            cost, curr, dep = heapq.heappop(heap)
            if curr == dst:
                ans = cost
                break  # 힙큐를 써서 이미 최단거리 확보했기 때문에 k제약 만족한 최단거리

            if dep <= K:
                for nxt in graph[curr]:
                    heapq.heappush(heap, (cost + nxt[0], nxt[1], dep + 1))
        return ans
