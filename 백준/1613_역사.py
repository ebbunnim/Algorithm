if __name__ == '__main__':
    V,E=map(int,input().split())
    INF=1e9
    dist=[[0]*V for _ in range(V)]

    for _ in range(E):
        a,b=map(int,input().split())
        dist[a-1][b-1]=1

    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][k] and dist[k][j]:
                    dist[i][j]=1

    s=int(input())
    for _ in range(s):
        a,b=map(int,input().split())
        if dist[a-1][b-1]==1:
            print(-1)
        elif dist[b-1][a-1]==1:
            print(1)
        else:
            print(0)
