from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    graph = defaultdict(list)
    for _ in range(N-1):
        a, b = map(int, input().split())
        graph[a]+=[b]
        graph[b]+=[a]

    parent = [0]*(N+1)
    stack = [1]

    while stack:
        curr = stack.pop()
        for nxt in graph[curr]:
            if parent[nxt]==0:
                parent[nxt]=curr
                stack.append(nxt)

    for x in parent[2:]:
        print(x)