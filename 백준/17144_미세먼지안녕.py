from copy import deepcopy
from math import floor


def spread_dust(x, y):
    global dusts
    dcur = floor(arr[x][y] / 5)

    for dx, dy in (1, 0), (-1, 0), (0, 1), (0, -1):
        nx, ny = x + dx, y + dy
        if 0 <= nx < R and 0 <= ny < C and arr[nx][ny] != -1:
            dusts[nx][ny] += dcur
            dusts[x][y] -= dcur


def move_dust():
    # 반시계 방향
    x1, y1 = machines[0][0], machines[0][1] + 1
    nx, ny = x1, y1
    after_move_dusts[nx][ny] = 0
    for dx, dy in (0, 1), (-1, 0), (0, -1), (1, 0):
        while (0 <= nx + dx < R and 0 <= ny + dy < C) and after_move_dusts[nx + dx][ny + dy] != -1:
            after_move_dusts[nx + dx][ny + dy] = arr[nx][ny]
            nx += dx
            ny += dy

            # 시계방향
    x2, y2 = machines[1][0], machines[1][1] + 1
    nx, ny = x2, y2
    after_move_dusts[nx][ny] = 0
    for dx, dy in (0, 1), (1, 0), (0, -1), (-1, 0):
        while (0 <= nx + dx < R and 0 <= ny + dy < C) and after_move_dusts[nx + dx][ny + dy] != -1:
            after_move_dusts[nx + dx][ny + dy] = arr[nx][ny]
            nx += dx
            ny += dy


if __name__ == '__main__':
    R, C, T = map(int, input().split())  # 행, 열, 이 시간 이후
    arr = [list(map(int, input().split())) for _ in range(R)]
    machines = []
    ans = 0

    for i in range(R):
        if arr[i][0] == -1:
            machines.append((i, 0))

    for _ in range(T):
        dusts = [[0] * C for _ in range(R)]  # 얘는 테케마다 초기화해줘야

        for i in range(R):
            for j in range(C):
                if arr[i][j] != -1 and arr[i][j] != 0:
                    spread_dust(i, j)
        for i in range(R):
            for j in range(C):
                if arr[i][j] != -1:
                    arr[i][j] += dusts[i][j]
        after_move_dusts = deepcopy(arr)  # 이제 움직인 걸 after move에 옮길거야
        after_move_dusts[machines[0][0]][machines[0][1]] = -1
        after_move_dusts[machines[1][0]][machines[1][1]] = -1
        move_dust()
        arr = deepcopy(after_move_dusts)

    for i in range(R):
        for j in range(C):
            if after_move_dusts[i][j] != 0:
                ans += after_move_dusts[i][j]
    print(ans + 2)


