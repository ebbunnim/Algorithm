import math

def solution(n, s, a, b, fares):
    INF = math.inf
    s, a, b = s - 1, a - 1, b - 1
    dist = [[INF] * (n) for _ in range(n)]
    for f in fares:
        dist[f[0] - 1][f[1] - 1] = f[2]
        dist[f[1] - 1][f[0] - 1] = f[2]

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):  # min연산 뒤 계속 재할당하면 시간초과 났었음
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    ans = INF
    for i in range(n):
        if ans > dist[s][i] + dist[i][a] + dist[i][b]:
            ans = dist[s][i] + dist[i][a] + dist[i][b]

    return ans