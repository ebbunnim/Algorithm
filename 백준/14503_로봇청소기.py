def move(x, y, d):
    global ans

    while True:
        nd = d
        flag = 0

        for _ in range(4):
            nd = (nd + 3) % 4  # 바뀐 방향을 계속 적용하며 돌아야한다.
            nx, ny = x + dx[nd], y + dy[nd]
            if 0 <= nx < N and 0 <= ny < M and vis[nx][ny] == False and arr[nx][ny] == 0:
                flag = 1
                vis[nx][ny] = True
                ans += 1
                x, y, d = nx, ny, nd  # 현재의 위치와 방향을 변화된 것으로 바꿔줘야 함
                break

        if flag == 0:  # 후진한다.
            x = x - dx[d]
            y = y - dy[d]
            # 후진했는데, 벽이면 탈출
            if arr[x][y] == 1:
                break


if __name__ == '__main__':
    N, M = map(int, input().split())
    r, c, d = map(int, input().split())
    vis = [[False] * M for _ in range(N)]
    arr = [list(map(int, input().split())) for _ in range(N)]
    ans = 1
    # 0 3 2 1 북 서 남 동
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]
    vis[r][c] = True
    move(r, c, d)
    print(ans)

