import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    M=int(input())
    N=int(input())
    sieze=[True]*(1+N)
    sieze[1]=False
    ubound=int(N**0.5)
    for i in range(2,ubound+1):
        if sieze[i]:
            for j in range(i*2,N+1,i):
                sieze[j]=False
    sumv=0
    flag=0
    for i in range(M,N+1):
        if sieze[i]:
            sumv+=i
            if not flag:
                minv=i
                flag=1
    if not flag:
        print(-1)
    else:
        print(sumv)
        print(minv)