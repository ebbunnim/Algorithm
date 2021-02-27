import sys
sys.stdin = open('input.txt','r')
input = sys.stdin.readline

if __name__ == '__main__':
    N, M, Q = map(int, input().split())
    p = list(map(int, input().split()))
    key = [(val, idx) for idx, val in enumerate(p)]
    key.sort()
    INF = sys.maxsize
    dist = [[INF]*N for _ in range(N)]

    penalty=[[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            penalty[i][j]=max(p[i],p[j])

    for i in range(N):
        dist[i][i] = penalty[i][i]

    for _ in range(M):
        a, b, d = map(int, input().split())
        a,b,d=a-1,b-1,d
        dist[a][b] = d+penalty[a][b]
        dist[b][a] = d+penalty[b][a]

    for k in key:  # 차례대로의 정점 번호가 아니라, penalty상으로 오름차순으로 가면 됨.
        val = k[0]
        idx = k[1]
        for i in range(N):
            for j in range(N):
                if i==j:
                    continue
                if dist[i][j]>dist[i][idx]-penalty[i][idx]+dist[idx][j]-penalty[idx][j]+max(val,penalty[i][idx],penalty[idx][j]):
                    dist[i][j]=dist[i][idx] - penalty[i][idx] + dist[idx][j] - penalty[idx][j] + max(val,penalty[i][idx],penalty[idx][j])
    for _ in range(Q):
        S, T = map(int, input().split())
        if dist[S-1][T-1] != INF:
            print(dist[S-1][T-1])
        else:
            print(-1)