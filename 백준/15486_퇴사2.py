import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N=int(input())
    P=[0]*(1+N)
    T=[0]*(1+N)
    D=[0]*(1+N)
    for i in range(N):
        t,p=map(int,input().split())
        P[i]=p
        T[i]=t
    for i in range(N):
        if i+T[i]<=N:
            D[i+T[i]]=max(D[i+T[i]],D[i]+P[i])
        D[i+1]=max(D[i],D[i+1]) # 일을 하지 않았어도, 이전까지 번 돈 pass
    print(max(D))
