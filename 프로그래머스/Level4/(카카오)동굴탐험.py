from collections import deque


def solution(n, path, order):
    graph = [[] for _ in range(n)]
    vis = [False] * n
    for p in path:
        graph[p[0]] += [p[1]]
        graph[p[1]] += [p[0]]
    fromto = dict()
    tofrom = dict()
    for o in order:
        fromto[o[0]] = o[1]  # key가 선행노드
        tofrom[o[1]] = o[0]  # key가 후행노드
    path = [False] * n

    def bfs():
        Q = deque([0])
        vis[0] = True
        while Q:
            curr = Q.popleft()
            path[curr] = True
            if tofrom.get(curr) is None:
                vis[curr] = True
                for nxt in graph[curr]:
                    if vis[nxt] == False:
                        Q.append(nxt)
                if fromto.get(curr) is not None and path[fromto[curr]] == True:  # jump
                    Q.append(fromto[curr])
            else:
                if vis[tofrom[curr]] == True:
                    vis[curr] = True
                    for nxt in graph[curr]:
                        if vis[nxt] == False:
                            Q.append(nxt)

    bfs()
    if False in path:
        return False
    else:
        return True
