import sys
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

if __name__ == '__main__':
    N,M=map(int,input().split())
    tgts=list(map(int,input().split()))
    Q=list(range(1,N+1))

    cnt=0
    for tgt in tgts:
        idx=Q.index(tgt)
        if N//2>=idx:
            cnt+=idx
        else:
            cnt+=N-idx
        Q=Q[idx+1:]+Q[:idx]
        N-=1

    print(cnt)
