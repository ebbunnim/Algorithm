import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N,S=map(int,input().split())
    Nlist=list(map(int,input().split()))
    s,e=0,0
    sumv,cnt=0,0
    ans=100000
    while e<=N:
        while sumv>=S and s<e:
            ans=min(ans,e-s)
            sumv-=Nlist[s]
            s+=1
        if e==N:
            break
        sumv+=Nlist[e]
        e+=1
    print(ans if ans!=100000 else 0)
