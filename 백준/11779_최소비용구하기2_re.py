import sys
import heapq
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def dijkstra(s):
    heap=[]
    heapq.heappush(heap,(0,s))
    dist=[INF]*(N+1)
    dist[s]=0
    while heap:
        cost,curr=heapq.heappop(heap)
        if dist[curr]<cost:
            continue
        for nxt in graph[curr]:
            ncost=cost+nxt[0]
            if dist[nxt[1]]>ncost:
                dist[nxt[1]]=ncost
                heapq.heappush(heap,(ncost,nxt[1]))
                trace[nxt[1]]=curr
    return dist[e]

if __name__ == '__main__':
    INF = int(1e10)
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(1+N)]
    for _ in range(M):
        s, e, cost = map(int, input().split())
        graph[s]+=[(cost,e)]
    s, e = map(int,input().split())
    trace=[-1]*(N+1)
    min_dist=dijkstra(s)
    path=[e]
    l=1
    while True:
        p=trace[e]
        if p==s:
            l+=1
            break
        path+=[p]
        l+=1
        e=p
    print(min_dist)
    print(l)
    print(s,end=' ')
    while path:
        print(path.pop(),end=' ')

# 메모리 : 129168KB
# 시간 : 228ms