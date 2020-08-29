from collections import deque

def solution(n, edge):
    graph = [[] for _ in range(len(edge))]
    for e in edge:
        graph[e[0]] += [e[1]]
        graph[e[1]] += [e[0]]
    info = [0] * (n + 1)  # 몇번 거쳐왔는지 더할 것 - 차수와 관련

    def bfs(start):
        q = deque()
        q.append((1, start))  # depth와 start
        info[start] = 1  # degree저장

        while q:
            depth, node = q.popleft()
            ndepth = depth + 1
            for e in graph[node]:
                if info[e] == 0:  # 아직 안들림
                    info[e] = ndepth
                    q.append((ndepth, e))

    bfs(1)
    maxv = max(info)
    return info.count(maxv)