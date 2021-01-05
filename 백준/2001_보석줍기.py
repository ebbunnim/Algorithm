from collections import deque

def bfs():
    global maxv
    Q = deque([(1, 0, 0)])
    vis[1][0] = True
    if 1 in island_with_jewel:
        Q.append((1, 1, 1<<0))
        vis[1][1<<0] = True
    while Q:
        curr, cnt, jewelries = Q.popleft()
        if curr == 1:
            maxv = max(maxv, cnt)
        for nxt in graph[curr]:
            # 보석을 줍지 않는다.
            if vis[nxt[1]][jewelries] == False and nxt[0] >= cnt:
                vis[nxt[1]][jewelries] = True
                Q.append((nxt[1], cnt, jewelries))
            # 주울 수 있다면 보석을 줍는다.
            if (nxt[1] in island_with_jewel):
                idx = island_with_jewel.index(nxt[1])
                if vis[nxt[1]][jewelries|(1<<idx)] == False and nxt[0] >= cnt:
                    vis[nxt[1]][jewelries|(1<<idx)] = True
                    Q.append((nxt[1], cnt+1, jewelries|(1<<idx)))

if __name__ == '__main__':
    n,m,k=map(int,input().split())
    island_with_jewel=[]
    graph=[[] for _ in range(1+n)]
    for _ in range(k):
        island_with_jewel+=[int(input())]
    for _ in range(m):
        a,b,c=map(int,input().split())
        graph[a]+=[(c,b)]
        graph[b]+=[(c,a)]
    vis=[[False]*(1<<14) for _ in range(101)]
    maxv=0
    bfs()
    print(maxv)