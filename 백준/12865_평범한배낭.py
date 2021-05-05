import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N,K=map(int,input().split())
    bags=[list(map(int,input().split())) for _ in range(N)]

    DP=[[0]*(K+1) for _ in range(N+1)] # 열-무게, 행-N번, 값-value
    for i in range(1,N+1):
        w,v=bags[i-1]
        for total_w in range(1,K+1):
            if w<=total_w: # 단위당 이득을 불릴 수 있으면 넣겠다.
                DP[i][total_w]=max(DP[i-1][total_w], DP[i-1][total_w-w]+v)
            else:
                DP[i][total_w]=DP[i-1][total_w]
    print(DP[N][K])







