import sys
sys.stdin = open('input.txt','r')

import heapq

def dijkstra(start):
    dist[start]=0
    heapq.heappush(heap,(0,start))
    
    while heap:
        cost,curr=heapq.heappop(heap)
        for nxt in graph[curr]:
            if dist[nxt[1]]<nxt[0]:
                continue
            ncost=cost+nxt[0]
            if dist[nxt[1]]>ncost:
                dist[nxt[1]]=ncost
                heapq.heappush(heap,(ncost,nxt[1]))

if __name__ == '__main__':
    T = int(input())
    for _ in range(T):
        n,d,c=map(int,input().split()) # 컴퓨터 개수 n, 간선개 개수 d, 해킹된 컴터번호 c
        graph = [[] for _ in range(n+1)]
        for _ in range(d):
            end,start,cost=map(int,input().split())
            graph[start]+=[(cost,end)]
        INF=int(1e9)
        dist=[INF]*(1+n)
        heap=[]

        dijkstra(c)
        cnt=maxv=0
        for e in dist:
            if e==INF:
                continue
            maxv = max(maxv,e)
            cnt+=1
        print(cnt,maxv)


