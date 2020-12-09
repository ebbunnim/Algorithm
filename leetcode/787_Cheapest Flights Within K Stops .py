
import heapq

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:       
        graph = [[] for _ in range(1+n)]
        for edge in flights:
            graph[edge[0]]+=[(edge[2],edge[1])]
        INF = 1e9
        distance = [INF]*(1+n)
        distance[src] = 0
        
        def djikstra(start):
            heap=[]
            heapq.heappush(heap, (0,start,0))
            
            while heap:
                cost, curr, cnt = heapq.heappop(heap)
                if cnt>K:
                    continue
                for nxt in graph[curr]:
                    if distance[nxt[1]] < nxt[0]:
                        continue
                    ncost = nxt[0]+cost
                    if ncost<distance[nxt[1]]:
                        distance[nxt[1]]=ncost
                        heapq.heappush(heap, (ncost,nxt[1],cnt+1))
                        
        djikstra(src)
        if distance[dst]==INF:
            return -1
        else:
            return distance[dst]
                