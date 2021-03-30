from collections import defaultdict, deque
import sys

minv = sys.maxsize
def solution(board, r, c):
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    kinds = set()
    friends = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                kinds.add(board[i][j])
                friends[board[i][j]] += [(i, j)]
    n = len(kinds)

    def can_go(r, c, vis):
        return 0 <= r < 4 and 0 <= c < 4 and not vis[r][c]

    def move(r, c, d, copy_board):
        while True:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if copy_board[nr][nc]:
                    return nr, nc
                else:
                    r, c = nr, nc
            else:
                return r, c

    def bfs(r, c, tr, tc, copy_board):  # 현재 위치, 타겟 위치
        Q = deque([(r, c, 0)])  # lv -> move에서는 lv의 의미가 확장됨
        vis = [[False] * 4 for _ in range(4)]  # vis가 현재 위치야? - 중복으로 갈 수 있지
        vis[r][c] = True
        while Q:
            r, c, lv = Q.popleft()
            if r == tr and c == tc:
                copy_board[r][c] = 0  # 항상 현재 위치는 0으로 만들어야
                return lv  # 이동 후 위치, 이동한 거리
            # +1씩 사방향
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if can_go(nr, nc, vis):
                    vis[nr][nc] = True
                    Q.append((nr, nc, lv + 1))
            # ctrl로 사방향
            for d in range(4):
                nr, nc = move(r, c, d, copy_board)
                if can_go(nr, nc, vis):
                    vis[nr][nc] = True
                    Q.append((nr, nc, lv + 1))

    def calc(cr,cc,r1,c1,r2,c2,copy_board):
        res=bfs(cr, cc, r1, c1, copy_board)+bfs(r1, c1, r2, c2, copy_board)+2
        return res

    vis = [False] * n
    def backtracking(cnt, stack, flags):
        global minv
        if cnt == n:  #
            res = 0
            copy_board = [b[:] for b in board]
            copy_r, copy_c = r, c  # 현재 커서
            for friend in stack:
                r1, c1 = friends[friend][flags[friend - 1]]
                r2, c2 = friends[friend][not flags[friend - 1]]
                res+=calc(copy_r,copy_c,r1,c1,r2,c2,copy_board)
                copy_r,copy_c=r2,c2
                # pruning
                if res >= minv:
                    return
            minv = min(minv, res)
            return

        for i in range(n):
            if not vis[i]:
                vis[i] = True
                stack += [i+1]

                flags[i] = 1
                backtracking(cnt+1, stack, flags)
                flags[i] = 0
                backtracking(cnt+1, stack, flags)

                stack.pop()
                vis[i] = False

    backtracking(0, [], [-1] * n)
    return minv







# board=[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
board=[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
# r,c=1,0
r,c=0,1

print(solution(board, r, c))

