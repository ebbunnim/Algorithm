from heapq import heappop, heappush

def bfs(x, y):
    global shark_eat, shark_size, dis, ans,vis

    while Q:

        dis, x, y = heappop(Q)

        if 0<arr[x][y]<shark_size: # 잡아먹는다.
            shark_eat += 1
            arr[x][y] = 0
            if shark_eat == shark_size:
                shark_size += 1
                shark_eat = 0
            # 초기화를 위한 작업. 물고기를 잡아먹으면, 그 자리에서 새롭게 bfs를 간다. 이전에 갔던곳도 다시 갈 수 있다.
            ans += dis
            dis = 0
            Q.clear()
            vis = [[False]*N for _ in range(N)]

        for dx, dy in [(1,0),(-1,0),(0,1),(0,-1)]:
            nx = x + dx
            ny = y + dy

            if 0<=nx<N and 0<=ny<N and vis[nx][ny] == False:
                # 큰 상어 나오면 움직일 수 없다.
                if arr[nx][ny] > shark_size:
                    continue
                # 더 작거나 같은 수, 그리고 0일때도 움직일 수 있다.
                heappush(Q,(dis+1,nx,ny))
                vis[nx][ny] = True

    return


if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    Q = []
    shark_size = 2
    shark_eat = 0
    dis = 0
    ans = 0

    vis = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 9:
                vis[i][j] = True
                arr[i][j] = 0
                heappush(Q, (dis,i,j))
                bfs(i,j)
                print(ans)
                exit()
