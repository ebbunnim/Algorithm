import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    N = int(input())
    arr = [list(input().split()) for _ in range(N)]
    vis = [[False]*N for _ in range(N)]

    students=[]
    for i in range(N):
        for j in range(N):
            if arr[i][j]=='S':
                students.append((i,j))

    def track_teacher(students):
        for s in students:
            for dr, dc in (-1,0),(1,0),(0,1),(0,-1):
                sr = s[0] # 초기화 주의
                sc = s[1]
                while True:
                    nr = sr+dr
                    nc = sc+dc
                    if 0<=nr<N and 0<=nc<N:
                        if arr[nr][nc]=='X':
                            sr, sc = nr, nc
                            continue
                        elif arr[nr][nc]=='T': # 선생님이면
                            return False
                        else: # 학생이거나 장애물
                            break
                    else:
                        break
        return True # 모든 학생들이 선생님 안마주침


    flag = 0
    def dfs(wall):
        global flag
        if flag == 1: # pruning
            return

        if wall==3:
            if track_teacher(students):
                flag = 1
            return

        for r in range(N):
            for c in range(N):
                if vis[r][c]==False and arr[r][c]=='X':
                    vis[r][c]=True
                    arr[r][c]='O'
                    dfs(wall+1)
                    vis[r][c]=False
                    arr[r][c]='X'

    dfs(0)
    if flag:
        print('YES')
    else:
        print('NO')

    # 그러지 말고, 그냥 'X'들에서 3개를 dfs로 찾고 되는지 확인하자
    # pruning: tracking teacher - 상하좌우 중 각 방향에서 S,T가 동시에 나오면 안된다.