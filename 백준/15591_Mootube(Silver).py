from collections import deque

def bfs(v,k):
    Q=deque([(0,v)])
    vis=[True]+[False]*N
    vis[v]=True
    cnt=0
    while Q:
        dist,curr=Q.popleft()
        for nxt in graph[curr]:
            if vis[nxt[1]]==False and nxt[0]>=k:
                vis[nxt[1]]=True
                Q.append(nxt)
                cnt+=1
    return cnt

if __name__ == '__main__':
    N,Q=map(int,input().split())
    graph=[[] for _ in range(N+1)]
    for _ in range(N-1):
        p,q,r=map(int,input().split())
        graph[p]+=[(r,q)] #dist,q
        graph[q]+=[(r,p)] #dist,p
    for _ in range(Q):
        k,v=map(int,input().split())
        print(bfs(v,k))