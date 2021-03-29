from itertools import permutations
from collections import defaultdict, deque
from copy import deepcopy

def solution(board, r, c):
    minv = 17
    dr, dc = [-1, 0, 1, 0], [0, 1, 0, -1]
    kinds = set()
    friends = defaultdict(list)
    for i in range(4):
        for j in range(4):
            if board[i][j]:
                kinds.add(board[i][j])
                friends[board[i][j]] += [(i, j)]
    n = len(kinds)
    permu = list(permutations(kinds, n))
    comb_vis=[False]*n
    res=[]

    def comb(s,n,cnt):
        res.append(tuple(comb_vis))
        if cnt==n:
            return
        for i in range(s,n):
            if comb_vis[i]==False:
                comb_vis[i]=True
                comb(i,n,cnt+1)
                comb_vis[i]=False
        return

    def can_go(r, c, vis):
        return 0 <= r < 4 and 0 <= c < 4 and not vis[r][c]

    def move(r, c, d):
        while True:
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < 4 and 0 <= nc < 4:
                if copy_board[nr][nc]:
                    return nr, nc
                else:
                    r, c = nr, nc
            else:
                return r, c

    def bfs(r, c, tr, tc):  # 현재 위치, 타겟 위치
        Q = deque([(r, c, 0)])  # lv -> move에서는 lv의 의미가 확장됨
        vis = [[False] * 4 for _ in range(4)] # vis가 현재 위치야? - 중복으로 갈 수 있지
        vis[r][c]=True
        while Q:
            r, c, lv = Q.popleft()
            if r == tr and c == tc:
                return r, c, lv  # 이동 후 위치, 이동한 거리
            # +1씩 사방향
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d]
                if can_go(nr, nc, vis):
                    vis[nr][nc] = True
                    Q.append((nr, nc, lv + 1))
            # ctrl로 사방향
            for d in range(4):
                nr, nc = move(r, c, d)
                if can_go(nr, nc, vis):
                    vis[nr][nc] = True
                    Q.append((nr, nc, lv + 1))

    comb(0,n,0)

    for p in permu:
        for i in range(len(res)): # friends[p[i]][res[i]]
            copy_board = deepcopy(board)
            copy_r, copy_c = r, c
            cnt = 0
            for j in range(n):
                # exec
                friend,flag=p[j],res[i][j]
                tr, tc = friends[friend][flag][0], friends[friend][flag][1]
                copy_r, copy_c, lv = bfs(copy_r, copy_c, tr, tc)  # curr -> target
                cnt += lv
                copy_board[tr][tc] = 0
                # same exec
                tr, tc = friends[friend][not flag][0], friends[friend][not flag][1]
                copy_r, copy_c, lv = bfs(copy_r, copy_c, tr, tc)  # target -> counter_target
                cnt += (lv + 2)
                copy_board[tr][tc] = 0
                if cnt>minv:
                    break
            minv = min(minv, cnt)
    # ans을 어떻게 카운트할지만 생각하면 됨!
    return minv


# board=[[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
board=[[3,0,0,2],[0,0,1,0],[0,1,0,0],[2,0,0,3]]
# r,c=1,0
r,c=0,1

print(solution(board, r, c))

# 입력
# 출력
# 전처리
# 순차적 - 함수화 / 알고리즘
