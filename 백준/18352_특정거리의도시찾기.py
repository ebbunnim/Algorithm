import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    N, M, K, X = map(int,input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e = map(int, input().split())
        graph[s]+=[e]
    Q = deque()
    distance = [-1]*(1+N)

    def bfs(start):
        Q.append((start,0))
        while Q:
            curr,depth = Q.popleft()

            for nxt in graph[curr]:
                if distance[nxt]==-1:
                    distance[nxt]=depth+1
                    Q.append((nxt,depth+1))

    bfs(X)

    flag=0
    for i in range(N+1): # asc
        if distance[i]==K:
            print(i)
            flag=1
    if flag == 1:
        print(-1)