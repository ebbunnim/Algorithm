import sys
sys.stdin = open('input.txt','r')

import heapq

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(1+N)]
    for _ in range(M):
        s, e, cost = map(int, input().split())
        graph[s]+=[(cost,e)]
    start, end = map(int,input().split())

    INF = int(1e9)
    distances = [INF]*(1+N)
    distances[start]=0
    heap=[]
    heapq.heappush(heap, (0,start))
    trace = [-1]*(1+N) # 이전 정보를 저장해둔다.

    while heap:
        cost, curr = heapq.heappop(heap)
        for nxt in graph[curr]: # (next cost, next node)
            if distances[nxt[1]] < nxt[0]:
                continue
            ncost = cost + nxt[0]
            if ncost < distances[nxt[1]]:
                heapq.heappush(heap, (ncost, nxt[1]))
                distances[nxt[1]] = ncost
                trace[nxt[1]] = curr # nxt[1]에 가기 위해 curr을 거쳤다.

    print(distances[end])
    res = [end]
    while True: # 역추적
        if trace[end]==-1:
            break
        res += [trace[end]]
        end = trace[end]
    print(len(res))
    while res:
        print(res.pop(), end=' ')

