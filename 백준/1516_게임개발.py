import sys
sys.stdin = open('input.txt','r')

from copy import deepcopy
from collections import deque

if __name__ == '__main__':
    # graph, indegree, time 필요
    N = int(input())
    graph = [[] for _ in range(1+N)]
    indegree = [0]*(1+N)
    time = [0]*(1+N)

    for i in range(1,N+1):
        tmp = list(map(int, input().split()))
        time[i] = tmp[0]
        for e in tmp[1:-1]:
            indegree[i] += 1
            graph[e].append(i)

    def topology_sort():
        res = deepcopy(time)
        Q = deque()
        # 진입차수 0인 노드부터 시작
        for i in range(1, N+1):
            if indegree[i]==0:
                Q.append(i)
        while Q:
            curr = Q.popleft()
            # 현재 원소와 연결된 노드들의 진입차수에서 1을 뺀다.
            for nxt in graph[curr]:
                res[nxt] = max(res[nxt],res[curr]+time[nxt])
                indegree[nxt] -= 1
                if indegree[nxt]==0:
                    Q.append(nxt)
        for i in range(1,N+1):
            print(res[i])

    topology_sort()
