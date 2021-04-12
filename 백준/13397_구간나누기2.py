import sys
sys.stdin = open('input.txt','r')

def bs():
    l,r=0,10001
    while l<r:
        mid=(l+r)//2 # (최대-최소)값 자체를 targeting
        # like two pointer
        minv,maxv=10001,0
        group=1
        for e in range(N):
            minv=min(minv,Nlist[e])
            maxv=max(maxv,Nlist[e])
            if (maxv-minv)<=mid:
                continue
            else: #  크다면 구간을 하나 늘린다.
                group+=1
                minv,maxv=Nlist[e],Nlist[e]
        if group<=M: # lower bound
            r=mid
        else:
            l=mid+1
    return r


if __name__ == '__main__':
    N,M=map(int,input().split())
    Nlist=list(map(int,input().split()))
    print(bs())



