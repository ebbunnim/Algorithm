from collections import deque


def solution(board):
    N = len(board[0])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    def can_go(nx, ny):
        return 0 <= nx < N and 0 <= ny < N and board[nx][ny] == 0

    def BFS(x, y, d):
        Q = deque()
        Q.append((x, y, d, 0))  # x,y,direction,cost
        check = [[0] * N for _ in range(N)]
        res = int(1e9)
        while Q:
            x, y, d, cost = Q.popleft()
            if x == N - 1 and y == N - 1:
                res = min(res, cost)
                continue
            for nd in range(4):
                nx = x + dx[nd]
                ny = y + dy[nd]
                if dx[d] == dx[nd] or dy[d] == dy[nd]:
                    ncost = cost + 100
                else:
                    ncost = cost + 600
                if can_go(nx, ny) and (not check[nx][ny] or check[nx][ny] > ncost):
                    check[nx][ny] = ncost
                    Q.append((nx, ny, nd, ncost))
        return res

    return min(BFS(0, 0, 1), BFS(0, 0, 3))