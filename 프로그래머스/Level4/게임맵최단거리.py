from collections import deque

def solution(maps):
    def can_go(r, c):
        return 0 <= r < n and 0 <= c < m and not vis[r][c] and maps[r][c]

    def bfs(r, c):
        Q = deque([(r, c, 1)])
        vis[r][c] = True
        while Q:
            r, c, lv = Q.popleft()
            if r == n - 1 and c == m - 1:
                return lv
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if can_go(nr, nc):
                    Q.append((nr, nc, lv + 1))
                    vis[nr][nc] = True
        return -1

    n, m = len(maps), len(maps[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    vis = [[False] * m for _ in range(n)]
    return bfs(0, 0)
