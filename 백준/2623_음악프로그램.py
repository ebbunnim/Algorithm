import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    V, N = map(int, input().split())
    graph = [[] for _ in range(1+V)]
    indegree = [0]*(1+V)
    for _ in range(N):
        s = list(map(int, input().split()))
        print(s)
        for i in range(1,len(s)-1):
            graph[s[i]].append(s[i+1])
            indegree[s[i+1]] += 1

    def topology_sort():
        res = []
        Q = deque()
        for i in range(1,V+1):
            if indegree[i]==0:
                Q.append(i)
        while Q :
            curr = Q.popleft()
            res.append(curr)
            for nxt in graph[curr]:
                indegree[nxt] -= 1
                if indegree[nxt]==0:
                    Q.append(nxt)
        if len(res) != V:
            print(0)
        else:
            for r in res:
                print(r)

    topology_sort()



