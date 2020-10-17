from collections import deque

board = [[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]

def solution(board):

    N = len(board)
    vis = [[[[False] * N for _ in range(N)] for _ in range(N)] for _ in range(N)]

    def move(L):  # L :{(r1,c1),(r2,c2)}
        r1 = L[0][0]
        c1 = L[0][1]
        r2 = L[1][0]
        c2 = L[1][1]
        candidates = []
        # 상하좌우
        for dr, dc in (-1, 0), (1, 0), (0, 1), (0, -1):
            nr1, nc1 = r1 + dr, c1 + dc
            nr2, nc2 = r2 + dr, c2 + dc
            if 0 <= nr1 < N and 0 <= nc1 < N and 0 <= nr2 < N and 0 <= nc2 < N:
                if board[nr1][nc1] == 0 and board[nr2][nc2] == 0:
                    candidates.append([(nr1, nc1), (nr2, nc2)])
        # 가로로 위치
        if r1 == r2:
            for d in [-1, 1]:
                nr1 = r1 + d
                nr2 = r2 + d
                if 0 <= nr1 < N and 0 <= nr2 < N:
                    if board[nr1][c1] == 0 and board[nr2][c2] == 0:  # 회전 중 벽 만나면 안되므로 and 조건
                        candidates.append([(r1, c1), (nr1, c1)])
                        candidates.append([(r2, c2), (nr2, c2)])
        # 세로로 위치
        elif c1 == c2:
            for d in [-1, 1]:
                nc1 = c1 + d
                nc2 = c2 + d
                if 0 <= nc1 < N and 0 <= nc2 < N:
                    if board[r1][nc1] == 0 and board[r2][nc2] == 0:
                        candidates.append([(r1, c1), (r1, nc1)])
                        candidates.append([(r2, c2), (r2, nc2)])
        return candidates

    Q=deque()
    Q.append(([(0,0),(0,1)],0))
    vis[0][0][0][1] = True

    while Q:
        q = Q.popleft()
        curr = q[0]
        t = q[1]

        if (N - 1, N - 1) in curr:
            break
        for nxt in move(curr):  # 다음 depth에 이동할 수 있는 노드들
            if vis[nxt[0][0]][nxt[0][1]][nxt[1][0]][nxt[1][1]] == False:
                vis[nxt[0][0]][nxt[0][1]][nxt[1][0]][nxt[1][1]] = True
                Q.append([nxt, t + 1])
    return t


print(solution(board))


# >>> a = {1,2}
# >>> a[0]
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# TypeError: 'set' object is not subscriptable
# set 자료형은 인덱스로 접근할 수 없다.