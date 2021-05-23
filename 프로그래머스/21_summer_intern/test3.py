# bfs였는데, 시작 rc가 선분 위에 걸쳐져 있는 케이스. 레벨 단위로 인덱스 재지정
from collections import deque

def solution(maps, p, r):
    n = len(maps[0])
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    max_killed = 0
    tgt_lv = r // 2

    def attack(r, c, lv, tgt_lv):
        if lv == tgt_lv:
            if maps[r][c] <= p // 2:
                return 1
        else:
            if maps[r][c] <= p:
                return 1
        return 0

    def bfs(r, c, tgt_lv):
        killed = 0
        Q = deque()
        vis = [[False] * n for _ in range(n)]

        # lv1 append
        for _dr, _dc in (-2, -2), (-2, -1), (-1, -2), (-1, -1):
            nr, nc = r + _dr, c + _dc
            if 0 <= nr < n and 0 <= nc < n:
                Q.append((nr, nc, 1))
                vis[nr][nc] = True

        while Q:
            r, c, lv = Q.popleft()
            if lv == tgt_lv + 1:
                return killed
                # attack
            killed += attack(r, c, lv, tgt_lv)
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if 0 <= nr < n and 0 <= nc < n and vis[nr][nc] == False:
                    vis[nr][nc] = True
                    Q.append((nr, nc, lv + 1))
        return 0

    for i in range(n + 2):
        for j in range(n + 2):
            max_killed = max(max_killed, bfs(i, j, tgt_lv))

    return max_killed

maps=[[1, 28, 41, 22, 25, 79, 4], [39, 20, 10, 17, 19, 18, 8], [21, 4, 13, 12, 9, 29, 19], [58, 1, 20, 5, 8, 16, 9], [5, 6, 15, 2, 39, 8, 29],[39, 7, 17, 5, 4, 49, 5], [74, 46, 8, 11, 25, 2, 11]]
p=19
r=6
print(solution(maps,p,r))
