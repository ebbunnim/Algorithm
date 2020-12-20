from collections import defaultdict

if __name__ == '__main__':
    N, M, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    shark_dirs = list(map(int, input().split()))
    priorites = [defaultdict(list) for _ in range(M)]
    for shark in range(M):
        for key in range(1, 5):
            priorites[shark][key] = list(map(int, input().split()))
    smells = [[[0, 0] for _ in range(N)] for _ in range(N)]  # [상어번호, 남은시간]
    dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 위, 아래, 왼쪽, 오른쪽


    # 상어가 움직이면 위치, 방향 정보 갱신
    def update(x, y, shark_num, nx, ny, nd):
        arr[x][y] = 0
        arr[nx][ny] = shark_num
        shark_dirs[shark_num - 1] = nd


    def shark_move(x, y, shark_num):
        D = priorites[shark_num - 1]
        priority = D[shark_dirs[shark_num - 1]]

        # smell 없는 쪽 우선 순회
        flag = 0
        for i in range(4):
            nx = x + dirs[priority[i] - 1][0]
            ny = y + dirs[priority[i] - 1][1]
            if 0 <= nx < N and 0 <= ny < N and smells[nx][ny] == [0, 0]:
                if arr[nx][ny] != 0:
                    arr[x][y] = 0
                else:
                    update(x, y, shark_num, nx, ny, priority[i])
                flag = 1
                break
        # smell이 있다면 현재 상어가 뿌린 궤적으로만 이동
        if flag == 0:
            for i in range(4):
                nx = x + dirs[priority[i] - 1][0]
                ny = y + dirs[priority[i] - 1][1]
                if 0 <= nx < N and 0 <= ny < N and smells[nx][ny][0] == shark_num:
                    update(x, y, shark_num, nx, ny, priority[i])
                    break


    tflag = t = 0
    while True:
        shark_list = []
        for x in range(N):
            for y in range(N):
                if arr[x][y] != 0:
                    shark_list += [(x, y, arr[x][y])]
        shark_list.sort(key=lambda x: x[2])

        # 냄새 잔여 시간 1씩 감소
        for x in range(N):
            for y in range(N):
                if smells[x][y][1] != 0:
                    smells[x][y][1] -= 1
                    if smells[x][y][1] == 0:
                        smells[x][y] = [0, 0]

        # 현재 상어 위치한다면 한번에 냄새 뿌리기 
        for x, y, num in shark_list:
            smells[x][y][0] = num
            smells[x][y][1] = K

        # 상어 움직임
        for x, y, num in shark_list:
            shark_move(x, y, num)

        # 탈출
        t += 1
        if t >= 1000:
            tflag = 1
            break
        if sum([sum(x) for x in arr]) == 1:
            break

    if tflag == 1:
        print(-1)
    else:
        print(t)