import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    V,E=map(int,input().split())
    INF=sys.maxsize
    dist=[[INF]*V for _ in range(V)]
    for i in range(V):
        dist[i][i]=0
    for _ in range(E):
        a,b,c=map(int,input().rstrip().split())
        dist[a-1][b-1]=c
    for k in range(V):
        for i in range(V):
            for j in range(V):
                if dist[i][j]>dist[i][k]+dist[k][j]:
                    dist[i][j]=dist[i][k]+dist[k][j]
    ans=INF
    for i in range(V):
        for j in range(i+1,V):
            if dist[i][j]!=INF:
                if dist[j][i]!=INF:
                    ans=min(ans,dist[i][j]+dist[j][i])
    print(ans if ans!=INF else -1)
