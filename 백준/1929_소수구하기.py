import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    M,N=map(int,input().split())
    sieve=[True]*(N+1)
    n=int(N**0.5)
    for i in range(2,n+1):
        if sieve[i]:
            for j in range(2*i,N+1,i):
                sieve[j]=False
    for i in range(M,N+1):
        if i==1:
            continue
        if sieve[i]:
            print(i)
