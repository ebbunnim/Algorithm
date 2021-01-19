import sys
import heapq
input=sys.stdin.readline

def dijkstra():
    dist[1]=0
    heap=[]
    heapq.heappush(heap,(0,1))
    while heap:
        cost,curr=heapq.heappop(heap)
        if dist[curr]<cost:
            continue
        for nxt in graph[curr]:
            ncost=cost+nxt[0]
            if ncost<dist[nxt[1]]:
                dist[nxt[1]]=ncost
                trace[nxt[1]]=curr
                heapq.heappush(heap,(ncost, nxt[1]))


if __name__ == '__main__':
    N,M=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for _ in range(M):
        a,b,c=map(int,input().split())
        graph[a]+=[(c,b)]
        graph[b]+=[(c,a)]
    INF=int(1e9)
    dist=[INF]*(1+N)
    trace=[-1]*(1+N)

    dijkstra()

    print(sum(1 for i in range(2,N+1) if dist[i]!=INF))
    for i in range(2,N+1):
        print(trace[i],i)
