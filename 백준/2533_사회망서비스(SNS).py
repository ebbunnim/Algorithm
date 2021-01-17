import sys
sys.stdin = open('input.txt','r')
sys.setrecursionlimit(10 ** 9)

def make_direction(curr):
    vis[curr] = True
    for nxt in graph[curr]:
        if vis[nxt] == False:
            child[curr] += [nxt]
            make_direction(nxt)

if __name__ == '__main__':
    N = int(sys.stdin.readline())
    graph = [[] for _ in range(N + 1)]
    child = [[] for _ in range(N + 1)]
    DP = [[-1] * (N + 1) for _ in range(2)]
    INF = 1e9
    for _ in range(N - 1):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a] += [b]
        graph[b] += [a]

    vis = [False] * (N + 1)
    make_direction(1)


    def dfs(curr, prev):
        if DP[prev][curr] != -1:
            return DP[prev][curr]
        on, off = 1, INF
        for nxt in child[curr]:
            on += dfs(nxt, True)
        if prev:
            off = 0
            for nxt in child[curr]:
                off += dfs(nxt, False)
        DP[prev][curr] = min(on, off)
        return DP[prev][curr]


    print(min(dfs(1, True), dfs(1, False)))
