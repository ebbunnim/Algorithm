import sys
sys.setrecursionlimit(1000000)

def solution(n, path, order):
    graph = [[] for _ in range(n)]
    for p in path:
        graph[p[0]] += [p[1]]
        graph[p[1]] += [p[0]]
    directed_graph = [[] for _ in range(n)]
    for o in order:
        directed_graph[o[1]] += [o[0]]

    def make_direction(src):
        vis[src] = True
        for nxt in graph[src]:
            if not vis[nxt]:
                make_direction(nxt)
                directed_graph[nxt] += [src]

    def detect_cycle(src):
        if vis[src]:
            return True
        if recur[src]:
            return False
        vis[src] = True
        recur[src] = True
        for nxt in directed_graph[src]:
            if detect_cycle(nxt):
                return True
        vis[src] = False
        return False

    vis = [False] * n
    make_direction(0)
    vis = [False] * n
    recur = [False] * n
    for src in range(n):
        if detect_cycle(src):
            return False
    return True