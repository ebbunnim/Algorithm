import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    penalty = list(map(int, input().split()))
    key = [(val, idx) for idx, val in enumerate(penalty)]
    key.sort()
    INF = sys.maxsize
    dist = [[INF]*N for _ in range(N)]
    dist_penalty = [[INF]*N for _ in range(N)]

    for i in range(N):
        dist[i][i] = 0

    for _ in range(M):
        a, b, d = map(int, input().split())
        a,b,d=a-1,b-1,d
        dist[a][b] = d
        dist[b][a] = d

    for k in key[1:]:  # 차례대로의 정점 번호가 아니라, penalty상으로 오름차순으로 가면 됨.
        val = k[0]
        idx = k[1]
        for i in range(N):
            for j in range(N):
                if i==j:
                    continue
                if dist[i][j] > dist[i][idx] + dist[idx][j]:
                    dist[i][j] = dist[i][idx] + dist[idx][j]
                max_penalty = max(penalty[i], penalty[j], val)
                if dist_penalty[i][j] > dist[i][idx] + dist[idx][j] + max_penalty:
                    dist_penalty[i][j] = dist[i][idx] + dist[idx][j] + max_penalty

    for _ in range(Q):
        S, T = map(int, input().split())
        if dist_penalty[S-1][T-1] != INF:
            print(dist_penalty[S-1][T-1])
        else:
            print(-1)