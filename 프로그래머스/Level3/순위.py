# 정확하게 순위가 매겨질 수 있었어야 함.
INF = int(1e9)


def solution(n, results):
    graph = [[INF] * (n + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        graph[i][i] = 0
    for res in results:
        graph[res[0]][res[1]] = 1

    for i in range(1, n + 1):
        for a in range(1, n + 1):
            for b in range(1, n + 1):
                graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

    trace = [0] * (n + 1)
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            if a != b and graph[a][b] == INF and graph[b][a] == INF:
                trace[b] = 1
    return trace.count(0) - 1

