import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N,M=map(int,input().split())
    l1=list(map(int,input().split()))
    l2=list(map(int,input().split()))
    l1+=[10**9+1]
    l2+=[10**9+1]
    s=e=0
    ans=[]
    while True:
        if s==N and e==M:
            break
        if l1[s]<=l2[e]:
            ans+=[l1[s]]
            s+=1
        else:
            ans+=[l2[e]]
            e+=1
    print(*ans)
