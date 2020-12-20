from copy import deepcopy

if __name__ == '__main__':
    arr = []
    for _ in range(4):
        tmp = list(map(int, input().split()))
        arr.append([[tmp[0],tmp[1]-1],[tmp[2],tmp[3]-1],[tmp[4],tmp[5]-1],[tmp[6],tmp[7]-1]]) # (물고기번호,방향)
    dirs = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]
    ans = 0

    def find_target_fish(arr,target):
        for i in range(4):
            for j in range(4):
                if arr[i][j][0]==target:
                    return (i,j)
        return False

    def if_fish_can_move(x,y,d,shark_x,shark_y):
        nx,ny = x+dirs[d][0], y+dirs[d][1]
        if 0 <= nx < 4 and 0 <= ny < 4 and not (nx == shark_x and ny == shark_y):
            return True
        return False

    def fish_move(arr,shark_x,shark_y):
        for target in range(1,17):
            fish = find_target_fish(arr,target)
            if fish:
                x, y = fish[0],fish[1]
                d = arr[x][y][1]
                if if_fish_can_move(x, y, d, shark_x, shark_y):
                    nx = x+dirs[d][0]
                    ny = y+dirs[d][1]
                    arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                else:
                    for _ in range(1,8):
                        d = (d+1)%8
                        if if_fish_can_move(x, y, d, shark_x, shark_y):
                            nx = x + dirs[d][0]
                            ny = y + dirs[d][1]
                            arr[x][y], arr[nx][ny] = arr[nx][ny], arr[x][y]
                            arr[nx][ny][1] = d  # 방향은 추가로 바꿔줌
                            break

    def make_shark_movelist(arr,shark_x, shark_y, shark_dir):
        movelist =[]
        for _ in range(3):
            shark_x+=dirs[shark_dir][0]
            shark_y+=dirs[shark_dir][1]
            if 0<=shark_x<4 and 0<=shark_y<4 and arr[shark_x][shark_y][0]!=-1:
                movelist+=[(shark_x,shark_y)]
        return movelist

    def dfs(arr,shark_x, shark_y,shark_eat):
        global ans

        # 상어 현위치
        arr = deepcopy(arr)
        shark_eat += arr[shark_x][shark_y][0] # 먹는다.
        arr[shark_x][shark_y][0]=-1 # 먹고 빈 공간 처리
        shark_dir = arr[shark_x][shark_y][1]

        # 물고기 이동
        fish_move(arr,shark_x,shark_y)

        # 상어 이동
        movelist = make_shark_movelist(arr,shark_x, shark_y,shark_dir)
        if movelist==[]:
            ans = max(ans, shark_eat)
            return
        for nx,ny in movelist:
            dfs(arr,nx,ny,shark_eat)

    dfs(arr,0,0,0)
    print(ans)
