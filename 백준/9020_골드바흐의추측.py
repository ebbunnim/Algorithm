import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        sieve=[True]*(1+N)
        n=int(N**0.5)
        for i in range(2,n+1):
            if sieve[i]:
                for j in range(2*i,N+1,i):
                    sieve[j]=False
        a,b=N,0
        for i in range(2,N//2+1):
            if sieve[i] and sieve[N-i]:
                if abs(a-b)>abs(i-(N-i)):
                    a,b=i,N-i
        print(a,b)


