import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    INF = int(1e9)
    n = int(input())
    m = int(input())
    graph = [[INF]*(n+1) for _ in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if i==j:
                graph[i][j] = 0
    for _ in range(m):
        s, e, cost = map(int,input().split())
        graph[s][e] = min(graph[s][e],cost) # 두 지점의 간선 하나가 아닐 수 있다면 더 최소를 넣겠다.
    for k in range(1,n+1):
        for a in range(1,n+1):
            for b in range(1,n+1):
                graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])

    for a in range(1, n+1):
        for b in range(1,n+1):
            if graph[a][b] ==INF:
                print(0,end=' ')
            else:
                print(graph[a][b],end=' ')
        print()
