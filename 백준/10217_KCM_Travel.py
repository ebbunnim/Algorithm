import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    T=int(input())
    INF=sys.maxsize
    for _ in range(T):
        N,M,K=map(int,input().split())
        cache=[[INF]*(1+M) for _ in range(1+N)]
        graph=[[] for _ in range(N+1)]
        for _ in range(K):
            u,v,c,d=map(int,input().split())
            graph[u]+=[(d,c,v)]
        cache[1][0]=0
        for cost in range(M+1):
            for src in range(1,N+1):
                if cache[src][cost]==INF:
                    continue
                for ele in graph[src]:
                    t,c,dst=ele
                    ncost=c+cost
                    if ncost<=M:
                        cache[dst][ncost]=min(cache[dst][ncost],cache[src][cost]+t)
        ans=min(cache[N][:])
        if ans==INF:
            print('Poor KCM')
        else:
            print(ans)


