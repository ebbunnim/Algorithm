from collections import deque


# 인접 행렬로 주어짐
def solution(n, computers):
    vis = [False] * n
    networks = 0

    def bfs(vis, start):
        Q = deque()
        Q.append(start)
        vis[start] = True

        while Q:
            curr = Q.popleft()
            for i in range(n):
                if computers[curr][i] == 1 and vis[i] == False:
                    vis[i] = True
                    Q.append(i)

    for i in range(n):  # 문제서 시작노드를 정해주지 않았음. vis==False인 상태를 시작 노드로
        if vis[i] == False:
            bfs(vis, i)
            networks += 1

    return networks