import sys
import heapq
input=sys.stdin.readline

def dijkstra(curr):
    heap=[]
    dist=[INF]*(1+N)
    dist[curr]=0
    heapq.heappush(heap,(0,curr))
    while heap:
        cost,curr=heapq.heappop(heap)
        if dist[curr]<cost:
            continue
        for nxt in graph[curr]:
            ncost=cost+nxt[0]
            if H[curr]<H[nxt[1]] and dist[nxt[1]]>ncost:
                dist[nxt[1]]=ncost
                heapq.heappush(heap,(ncost,nxt[1]))
    return dist


if __name__ == '__main__':
    N,M,D,E=map(int,input().split())
    H=[0]+list(map(int,input().split()))
    INF=int(1e12)
    graph=[[] for _ in range(1+N)]
    for _ in range(M):
        a,b,c=map(int,input().split())
        graph[a]+=[(c,b)]
        graph[b]+=[(c,a)]
    home_to_target=dijkstra(1) # home -> target
    campus_to_target=dijkstra(N) # campus_to_target
    value=-INF
    for target in range(2,N):
        tmp=0
        if home_to_target[target]==INF or campus_to_target[target]==INF:
            continue
        tmp+=(H[target]*E-home_to_target[target]*D)
        tmp-=(campus_to_target[target]*D)
        value=max(value,tmp)
    print(value if value!=-INF else "Impossible")
