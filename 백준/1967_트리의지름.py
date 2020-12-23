from collections import deque


def bfs(start):
    Q = deque([(0, start)])
    vis[start] = True
    while Q:
        dist, curr = Q.popleft()
        for nxt in graph[curr]:
            if vis[nxt[1]] == False:
                vis[nxt[1]] = True
                Q.append((dist + nxt[0], nxt[1]))
                distance[nxt[1]] = dist + nxt[0]


if __name__ == '__main__':
    N = int(input())
    graph = [[] for _ in range(1 + N)]
    for _ in range(N - 1):
        n1, n2, edge = map(int, input().split())
        graph[n1] += [(edge, n2)]
        graph[n2] += [(edge, n1)]

    distance = [0] * (1 + N)
    vis = [True] + [False] * N
    bfs(1)

    u = distance.index(max(distance))

    distance = [0] * (1 + N)
    vis = [True] + [False] * N
    bfs(u)

    print(max(distance))