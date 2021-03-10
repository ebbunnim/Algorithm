import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        DP=[[0,0,0,0] for _ in range(N+1)]
        DP[1][1]=1
        DP[2][1]=1
        DP[2][2]=1
        DP[3][1]=1
        DP[3][2]=1
        DP[3][3]=1
        for i in range(4,N+1):
            DP[i][1]=DP[i-1][1]
            DP[i][2]=DP[i-2][1]+DP[i-2][2]
            DP[i][3]=DP[i-3][1]+DP[i-3][2]+DP[i-3][3]
        print(sum(DP[N]))


