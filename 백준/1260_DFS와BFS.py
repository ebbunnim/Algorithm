import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    N,M,V = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    # 양방향 그래프로 만들기
    for i in range(M):
        n1,n2 = map(int, input().split())
        graph[n1] += [n2]
        graph[n2] += [n1]
    for i in range(1,N+1):
        graph[i].sort()

    vis = [True] + [False] * N
    vis[V] = True
    def DFS(V):
        print(V, end=' ')
        if False not in vis:
            return
        for node in graph[V]:
            if vis[node] == False:
                vis[node] = True
                DFS(node)
        return

    def BFS(V):
        vis = [True] + [False] * N
        Q = deque([V]) # start
        vis[V] = True
        while Q:
            node = Q.popleft()
            print(node, end=' ')
            for node2 in graph[node]:
                if vis[node2] == False:
                    Q.append(node2)
                    vis[node2] = True
        return

    DFS(V)
    print()
    BFS(V)