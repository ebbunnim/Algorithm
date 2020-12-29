import heapq

def dijkstra(start):
    dist[start]=0
    heapq.heappush(heap,(0,start))
    while heap:
        cost,curr=heapq.heappop(heap)
        for nxt in graph[curr]:
            if dist[nxt[1]]<nxt[0]: # start->nxt로 갈건데 이미 작으면 갱신 안함.
                continue
            ncost=cost+nxt[0] # 이후 한번 더 curr cost 더한 ncost로 확인.
            if dist[nxt[1]]>ncost:
                dist[nxt[1]]=ncost
                heapq.heappush(heap,(ncost,nxt[1]))

if __name__=='__main__':
    nums = [4, 1, 2, 3, 1, 0, 5]
    n = len(nums)
    graph = [[] for _ in range(n)]

    for node, val in enumerate(nums):
        if 0 <= (node - val) <= n - 1:
            graph[node] += [(1, node - val)]
        if 0 <= node + val <= n - 1:
            graph[node] += [(1, node + val)]

    INF = int(1e9)
    dist = [INF] * n
    heap = []

    dijkstra(0)

    if dist[n-1]!=INF:
        print(dist[n-1])
    else:
        print(-1)