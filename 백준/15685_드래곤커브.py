def curve(x, y, d, g):
    stack = []
    stack.append((d))
    vis[x + dx[d]][y + dy[d]] = True
    nx, ny = x + dx[d], y + dy[d]  ## nx,ny는 계속 바로 전이랑 이어져야 함. 스택이랑은 무관하게
    for i in range(g):
        L = len(stack)
        for j in range(L - 1, -1, -1):
            d = stack[j]  # 스택은 누적되어야함.pop하면 안됨.
            nd = (d + 1) % 4
            nx, ny = nx + dx[nd], ny + dy[nd]
            stack.append((nd))
            vis[nx][ny] = True
    return


if __name__ == '__main__':
    N = int(input())
    vis = [[False] * 101 for _ in range(101)]
    dx = [0, -1, 0, 1]
    dy = [1, 0, -1, 0]

    for _ in range(N):
        y, x, d, g = map(int, input().split())  # y열, x행, 방향, 세대
        vis[x][y] = True
        curve(x, y, d, g)

    ans = 0
    for i in range(100):
        for j in range(100):
            if vis[i][j] == True:
                if vis[i + 1][j] == True and vis[i][j + 1] == True and vis[i + 1][j + 1] == True:
                    ans += 1
    print(ans)
