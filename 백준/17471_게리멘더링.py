import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    N = int(input())
    people = [0]+list(map(int, input().split()))
    graph = [[] for _ in range(1+N)]
    vis = [False]*(1+N)
    for i in range(1,N+1):
        tmp = list(map(int, input().split()))
        graph[i].extend(tmp[1:])
    ans = 1000

    def is_connected(group,flag): # not connected하면 -1을 반환한다. connected 하다면 총 인구수를 반환한다.
        Q = deque()
        Q.append(group[0])
        subvis = [False]*(1+N)
        subvis[group[0]]=True
        while Q:
            curr = Q.popleft()
            for nxt in graph[curr]:
                if vis[nxt]==flag and subvis[nxt]==False:
                    subvis[nxt]=True
                    Q.append(nxt)
        sumv=0
        for g in group:
            if subvis[g]==False:
                return -1
            sumv += people[g]
        return sumv



    def comb(cnt,depth):
        global ans
        if cnt == depth:
            G1 = []
            G2 = []
            for i in range(1,N+1):
                if vis[i]==False:
                    G1.append(i)
                else:
                    G2.append(i)
            # if is_connected
            a = is_connected(G1,False)
            b = is_connected(G2,True)
            if a!=-1 and b!=-1:
                ans = min(ans,abs(a-b))
            return

        for i in range(1,N+1): # 부모 노드들. 시작점이 안정해져 있으므로 독립적인 parent 역할을 함 (정해져 있으면 자식노드로 바로 갔을 것)
            if vis[i]==False:
                vis[i]=True
                res.append(i)
                comb(cnt+1,depth)
                vis[i]=False
                res.pop()

    for depth in range(1,N//2+1):
        res=[]
        comb(0,depth)
    if ans == 1000:
        print(-1)
    else:
        print(ans)


    # 두 집단을 나누고 - 어떻게 나누냐? - 조합. NC(N//2) 까지 + 연결되어 있는지 bfs로 확인
    # 각 집단을 더해서 비교. 그 차이가 최소가 되도록 저장하기