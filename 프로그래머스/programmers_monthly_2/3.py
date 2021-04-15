from collections import deque

def solution(a, edges):
    if sum(a):
        return -1

    graph = [[] for _ in range(len(a))]
    for e in edges:
        graph[e[0]] += [e[1]]
        graph[e[1]] += [e[0]]

    starts = []
    for i in range(len(a)):
        if len(graph[i]) == 1:
            starts += [i]

    cnt=sum([1 for e in a if e])
    vis = [False] * len(a)
    Q = deque(starts)
    for start in starts:
        vis[start] = True

    ans = 0
    while Q:
        curr = Q.popleft()
        if cnt == 1:
            break
        if a[curr] != 0:
            cnt -= 1
            ans += abs(a[curr])
        for nxt in graph[curr]:
            if not vis[nxt]:
                vis[nxt] = True
                Q.append(nxt)
    return ans