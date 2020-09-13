import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    N, M = map(int, input().split())  #노드번호, 간선정보
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        start, end = map(int, input().split())
        graph[start].append((1,end)) # 비용, 목표노드
        graph[end].append((1,start))
    INF = int(1e9)
    distance = [INF]*(N+1)
    heap = []
    def dijkstra(start):
        heapq.heappush(heap, (0,start)) # 비용, 노드
        distance[start] = 0
        while heap:
            dist, node = heapq.heappop(heap)
            if distance[node] < dist: # 이미 갱신된 상태다.
                continue
            for i in graph[node]:
                cost = dist + i[0] # 다음 비용 (현재 비용 + 다음 노드 비용)
                if cost < distance[i[1]]:
                    distance[i[1]] = cost
                    heapq.heappush(heap, (cost, i[1]))
    dijkstra(1)
    for i in range(N+1):
        if distance[i]==INF:
            distance[i]=-1
    maxv = max(distance)
    ans = 0
    flag = 0
    cnt = 0
    for i in range(N+1):
        if distance[i]==maxv:
            if flag == 0:
                ans = i
                flag = 1
            cnt += 1
    print(str(ans) +' '+str(maxv)+' '+str(cnt))


