import sys
import heapq
input=sys.stdin.readline

def dijkstra(start):
    heap=[]
    dist=[INF]*(1+n)
    dist[start]=0
    heapq.heappush(heap,(0,start))
    while heap:
        cost,curr=heapq.heappop(heap)
        if dist[curr]<cost:
            continue
        for nxt in graph[curr]:
            ncost=cost+nxt[0]
            if dist[nxt[1]]>ncost:
                dist[nxt[1]]=ncost
                heapq.heappush(heap,(ncost,nxt[1]))
    return dist

if __name__ == '__main__':
    for _ in range(int(input())):
        n,m,t=map(int,input().split())
        s,g,h=map(int,input().split())
        graph=[[] for _ in range(1+n)]
        INF=sys.maxsize
        for _ in range(m):
            a,b,d=map(int,input().split())
            graph[a]+=[(d,b)]
            graph[b]+=[(d,a)]
        s_table=dijkstra(s)
        g_table=dijkstra(g)
        h_table=dijkstra(h)
        ans=set()
        for _ in range(t):
            target=int(input())
            if g_table[h]+min(s_table[g]+h_table[target],s_table[h]+g_table[target])==s_table[target]:
                ans.add(target)
        print(*sorted(ans))

