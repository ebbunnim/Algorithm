from collections import deque

# 이어지지 않은 것은, 따로 카운트해야 한다.
def solution(n, computers):
    vis = [False] * n
    ans = 0
    for i in range(n):
        if vis[i] == False:
            bfs(i, vis, n, computers)
            ans += 1

    return ans


def bfs(start_node, vis, n, computers):
    Q = deque()
    Q.append(start_node)  # 시작되는 노드
    vis[start_node] = True

    while Q:
        node = Q.popleft()
        for i in range(n):  # 열 또는 행이라고 생각하고
            if vis[i] == False:
                if computers[i][node] == 1:
                    vis[i] = True
                    Q.append(i)
    return