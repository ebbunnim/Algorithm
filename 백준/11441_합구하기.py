import sys
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    Nlist=list(map(int,input().split()))
    prefix_sum=[0]*(1+N)
    for i in range(1,N+1):
        prefix_sum[i]=Nlist[i-1]+prefix_sum[i-1]
    M=int(input())
    for _ in range(M):
        a,b=map(int,input().split())
        print(prefix_sum[b]-prefix_sum[a-1])