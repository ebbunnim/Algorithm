import sys

def solution(n, s, a, b, fares):
    INF = sys.maxsize
    dist = [[INF] * n for _ in range(n)]
    for f in fares:
        dist[f[0] - 1][f[1] - 1] = f[2]
        dist[f[1] - 1][f[0] - 1] = f[2]

    for i in range(n):
        dist[i][i] = 0

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][j] > dist[i][k] + dist[k][j]: # min으로 계속 재할당하면 시간초과 났었음
                    dist[i][j] = dist[i][k] + dist[k][j]

    ans = INF
    for i in range(n):
        res = dist[s - 1][i] + dist[i][a - 1] + dist[i][b - 1]
        if ans > res:
            ans = res
    return ans
