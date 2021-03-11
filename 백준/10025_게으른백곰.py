import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N,K=map(int,input().split())
    arr=[0]*1000001
    maxv,minv=0,100000
    for _ in range(N):
        g,x=map(int,input().split())
        if x>maxv:
            maxv=x
        if x<minv:
            minv=x
        arr[x]=g # x 좌표에 들어있는 얼음양
    start=(0 if minv-K<0 else minv-K)
    e=start
    sumv,ans=0,0
    for s in range(start,maxv+1): # minv~maxv의 모든 범위의 값들을 left pointer로 잡는다. 윈도우 크기는 최대 2*K
        while e<=1000000 and e-s<=2*K:
            sumv+=arr[e]
            e+=1
        ans=max(ans,sumv)
        sumv-=arr[s]
    print(ans)
