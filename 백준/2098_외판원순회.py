def tsp(curr, vis):
    if vis == (1 << N) - 1:
        return dist[curr][0]

    if D[curr][vis] != INF:
        return D[curr][vis]

    res = 1e9
    for nxt in range(N):
        if vis & (1 << nxt) == 0 and dist[curr][nxt] != INF:
            res = min(res, tsp(nxt, vis | (1 << nxt)) + dist[curr][nxt])
    D[curr][vis] = res
    return res


if __name__ == '__main__':
    N = int(input())
    dist = [list(map(int, input().split())) for _ in range(N)]
    INF = int(1e9)

    for i in range(N):
        for j in range(N):
            if i != j and dist[i][j] == 0:
                dist[i][j] = INF

    D = [[INF] * (1 << N) for _ in range(N)]

    print(tsp(0, 0))
