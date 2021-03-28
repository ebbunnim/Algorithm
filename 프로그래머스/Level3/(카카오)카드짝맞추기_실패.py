from itertools import permutations
from collections import defaultdict, deque
from copy import deepcopy


def solution(board, r, c):
    answer = 0
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    friends = defaultdict(list)
    ancestor_board = deepcopy(board)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                friends[board[i][j]] += [(i, j)]
    permu = list(permutations(friends.keys(), 3))

    def bfs(r, c, friend, d):  # 현재 커서 -> 원소 -> 대응 원소 이때 최단 거리에 두번을 써야 한다.
        # board를 돌면서 friend 색이 같은 애를 찾는다.
        Q = deque([(r, c, 0, -1)])
        vis = [[False] * 4 for _ in range(4)]
        vis[r][c] = True
        while Q:
            r, c, lv, d = Q.popleft()
            for nd in range(4):
                nr, nc = r + dr[nd], c + dc[nd]
                if 0 <= nr < 4 and 0 <= nc < 4 and not vis[nr][nc]:
                    if board[nr][nc]:
                        if (nr, nc) == friend:  # 색이랑 똑같다고 한다면,
                            board[nr][nc] = 0
                            return nr, nc, lv  # 반드시 찾게 되어있다.
                        else:  # 색이 같지 않다,
                            if d == nd:
                                vis[nr][nc] = True
                                Q.append((nr, nc, lv, nd))
                            else:
                                vis[nr][nc] = True
                                Q.append((nr, nc, lv + 1, nd))
                    else:  # lv은 건드리지 않는다.
                        vis[nr][nc] = True
                        Q.append((nr, nc, lv, nd))
        return -1, -1, -1

    minv = 17
    for i in range(len(permu)):
        for j in range(2):
            cnt = 0
            board = deepcopy(ancestor_board)
            nr, nc = r, c  # start는 보존
            for friend in permu[i]:
                nr, nc, lv = bfs(nr, nc, friends[friend][j], -1)  # 현재 커서 -> target
                cnt += lv
                nr, nc, lv = bfs(nr, nc, friends[friend][not j], -1)  # target -> counter target
                cnt += (lv + 2)  # enter 횟수 추가
            if cnt < minv:
                minv = cnt
    return minv

