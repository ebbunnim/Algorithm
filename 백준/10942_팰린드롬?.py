import sys
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    Nlist=input().split()
    M=int(input())
    DP=[[0]*N for _ in range(N)]

    for i in range(N): 
        DP[0][i]=1 
    for i in range(N-1):
        DP[1][i]=(1 if Nlist[i]==Nlist[i+1] else 0)
    for i in range(2,N):
        for j in range(N-i):
            if Nlist[j]==Nlist[j+i] and DP[i-2][j+1]:
                DP[i][j]=1

    for _ in range(M):
        s,e=map(int,input().split())
        print(DP[e-s][s-1])
