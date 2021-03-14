import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N=int(input())
    Nlist=list(map(int,input().split()))
    # 현재 다 소수로 간주
    sieve=[True]*1001
    maxv=max(Nlist)
    m=int(maxv**0.5)
    for i in range(2,m+1):
        if sieve[i]:
            for j in range(2*i,maxv+1,i):
                sieve[j]=False
    ans=0
    for n in Nlist:
        if n==1:
            continue
        if sieve[n]:
            ans+=1
    print(ans)
