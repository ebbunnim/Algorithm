import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    DP=[i for i in range(1+N)]
    if N<=5:
        print(N)
    else:
        for i in range(6,N+1):
            DP[i]=max(DP[i-1]+1,DP[i-3]*2,DP[i-4]*3,DP[i-5]*4)
        print(DP[N])
