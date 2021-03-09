import sys
sys.setrecursionlimit(10**6)
sys.stdin = open('input.txt','r')
input=sys.stdin.readline

def is_cycle(src):
    if vis[src]:
        return src # cycle 발생 지점
    if recur[src]:
        return  # pruning
    vis[src]=True
    recur[src]=True
    v=is_cycle(students[src])
    vis[src]=False
    if v: # cycle발생한 경우라면
        cycle[src]=True
        if src!=v:
            return v

if __name__ == '__main__':
    T=int(input())
    for _ in range(T):
        N=int(input())
        vis=[False]*(N+1)
        recur=[False]*(N+1)
        cycle=[False]*(N+1)
        students=[0]+list(map(int,input().split()))
        for i in range(1,N+1):
            is_cycle(i)
        print(N-sum(cycle))
