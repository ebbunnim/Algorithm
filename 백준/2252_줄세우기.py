from collections import deque

def topology_sort():
    Q = deque([idx for idx, val in enumerate(indegree) if val == 0])
    while Q:
        curr = Q.popleft()
        print(curr, end=' ')
        for nxt in graph[curr]:
            indegree[nxt] -= 1
            if indegree[nxt] == 0:
                Q.append(nxt)

if __name__ == '__main__':
    N,M=map(int,input().split())
    indegree=[-1]+[0]*N
    graph=[[] for _ in range(1+N)]
    for _ in range(M):
        a,b=map(int,input().split())
        graph[a]+=[b]
        indegree[b]+=1
    topology_sort()