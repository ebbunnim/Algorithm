from collections import deque

def topolopy_sort():
    Q = deque()
    for x in range(N + 1):
        if indegree[x] == 0:
            Q.append(x)
            D[x] = delays[x]
    while Q:
        curr = Q.popleft()
        for nxt in graph[curr]:
            indegree[nxt] -= 1
            D[nxt] = max(D[nxt], D[curr] + delays[nxt])
            if indegree[nxt] == 0:
                Q.append(nxt)
    print(D[W])

if __name__ == '__main__':
    T=int(input())
    for t in range(T):
        N,K=map(int,input().split())
        delays=[0]+list(map(int,input().split()))
        indegree=[-1]+[0]*N
        graph=[[]*(1+N) for _ in range(1+N)]
        for _ in range(K):
            s,e=map(int,input().split())
            graph[s]+=[e]
            indegree[e]+=1
        W=int(input())

        D=[0]*(1+N)
        topolopy_sort()