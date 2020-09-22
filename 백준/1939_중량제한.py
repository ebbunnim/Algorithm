import sys
sys.stdin = open('input.txt','r')

from collections import deque

if __name__ == '__main__':
    V, E = map(int, input().split())
    graph = [[] for _ in range(1+V)]
    for _ in range(E):
        A, B, C = map(int, input().split())
        graph[A] += [(B,C)]
        graph[B] += [(A,C)]
    S, E = map(int, input().split())
    # lower_bound + max
    # 1->3 에서 끝내는게 아님, 다른 루트를 통해서 가도 더 중량제한이 높을 수 있다.
    def bfs(start,end, target):
        Q = deque([start]) # node
        vis = [True] + [False] * V
        vis[start] = True
        while Q :
            curr = Q.popleft()
            for nxt in graph[curr]:
                if vis[nxt[0]] == False and target <= nxt[1]:# lowerbound
                    vis[nxt[0]] = True
                    Q.append(nxt[0])
        if vis[end] == True:
            return True
        else:
            return False
    s, e = 0, 1000000000
    ans = 0
    while s<=e:
        target = (s+e)//2
        if bfs(S,E,target):
            s = target + 1
            ans = target
        else:
            e = target -1
    print(ans)

