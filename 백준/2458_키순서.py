import sys
sys.stdin = open('input.txt','r')


if __name__ == '__main__':
    N,M = map(int, input().split())
    INF = 1e9
    graph = [[INF]*(1+N) for _ in range(1+N)]
    for i in range(1,N+1):
        graph[i][i]=0
    for _ in range(M):
        a, b = map(int, input().split())
        graph[a][b]=1 # 단방향

    for k in range(1,N+1):
        for a in range(1,N+1):
            for b in range(1,N+1):
                graph[a][b] = min(graph[a][b],graph[a][k]+graph[k][b])
    res = []
    for node in range(1,N+1):
        tmp =[]
        for node2 in range(1,N+1):
            if graph[node][node2]==INF:
                tmp.append(node2)
        flag = 0
        for node2 in tmp:
            if graph[node2][node]==INF:
                flag = 1
                break
        if flag == 0:
            res.append(node)
    print(len(res))
