import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N,M=map(int,input().split())
    mems=list(map(int,input().split()))
    costs=list(map(int,input().split()))
    max_cost=sum(costs)
    DP=[[0]*(max_cost+1) for _ in range(N)]
    INF=sys.maxsize
    res=INF
    for i in range(N):
        for cost in range(1,max_cost+1):
            if costs[i]<=cost:
                DP[i][cost]=max(DP[i-1][cost],DP[i-1][cost-costs[i]]+mems[i])
            else:
                DP[i][cost]=DP[i-1][cost]
            if DP[i][cost]>=M:
                res=min(res,cost)
    if res!=INF:
        print(res)
    else:
        print(0)
