import sys
import heapq
input=sys.stdin.readline

def topology_sort():
    tmp=[i for i in range(1,N+1) if indegree[i]==0]
    heap=[]
    for t in tmp:
        heapq.heappush(heap,t)
    while heap:
        curr=heapq.heappop(heap)
        print(curr,end=' ')
        for nxt in graph[curr]:
            indegree[nxt]-=1
            if indegree[nxt]==0:
                heapq.heappush(heap,nxt)
    return

if __name__ == '__main__':
    N,M=map(int,input().split())
    graph=[[] for _ in range(1+N)]
    indegree=[-1]+[0]*N
    for _ in range(M):
        s,e=map(int,input().split())
        graph[s]+=[e]
        indegree[e]+=1
    topology_sort()