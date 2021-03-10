import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    DP=[[0]*N for _ in range(N)]
    # start
    DP[0][0]=1
    for i in range(N):
        for j in range(N):
            if i==N-1 and j==N-1: # (N-1,N-1)일때 arr값은 0이므로 덮어쓸 위험 있기 때문
                break
            d=arr[i][j]
            if i+d<N:
                DP[i+d][j]+=DP[i][j]
            if j+d<N:
                DP[i][j+d]+=DP[i][j]
    print(DP[N-1][N-1])
