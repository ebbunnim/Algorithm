import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    N = int(input())
    M = int(input())
    graph = [[] for _ in range(N+1)]
    vis = [True] + [False]*N
    for _ in range(M):
        n1,n2 = map(int, input().split())
        graph[n1] += [n2]
        graph[n2] += [n1]
    def bfs():
        cnt = 0
        Q = deque([1]) # start node
        vis[1] = True
        while Q :
            curr = Q.popleft()
            for nxt in graph[curr]:
                if vis[nxt] == False:
                    vis[nxt] = True
                    Q.append(nxt)
                    cnt += 1
        return cnt
    print(bfs())


