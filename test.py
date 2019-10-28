import sys
sys.stdin = open("input.txt", "r")
from collections import deque

# 그대로 하면 무한루프에 걸림 


def safe(x, y):
    return 0<=x<N and 0<=y<M

def melt(x, y):
    cnt=0
    for i in range(4):
        idx = x + D[i][0]
        idy = y + D[i][1]
        if safe(idx, idy) and arr[idx][idy] == -1:
            cnt+=1
            if cnt ==2 :
                # 두 면이 공기와 만난 상태라면 일단 2라고 상태표시하고 break함
                arr[x][y] = 2
                break

# 외부공기와 안쪽 구명을 다르게 취급하기 위해서 상태표시 다르게 함
def bfs(x, y):
    Q.append((x, y))
    vis[x][y] = True
    arr[x][y] = -1
    while Q:
        a = Q.popleft()
        for i in range(4):
            idx = a[0] + D[i][0]
            idy = a[1] + D[i][1]
            # index 범위를 조건문 앞에서 먼저 sorting해야
            if safe(idx, idy) and arr[idx][idy] == 0 and vis[idx][idy] == False:
                Q.append((idx, idy))
                vis[idx][idy] = True
                arr[idx][idy] = -1

if __name__=="__main__":
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vis=[[False]*M for _ in range(N)]; Q=deque(); ans=0
    D = [(1,0), (-1,0), (0,1), (0,-1)]
    # 가장 처음에는 치즈가 올려있지 않다고 했으므로,
    bfs(0, 0)


    while arr != [[-1]*M for _ in range(N)]:
        ans += 1
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 1:
                    melt(i, j)
        # 다시 -1로 바꿔준다.
        for i in range(N):
            for j in range(M):
                if arr[i][j] == 2:
                    arr[i][j] = -1

        for i in range(N):
            for j in range(M):
                if arr[i][j] == 0:
                    for i in range(4):
                        idx = i + D[i][0]
                        jdx = j + D[i][0]
                        # 외부공기와 맞닿아있으면 더 이상 구멍이 아님.
                        if arr[idx][jdx] == -1:
                            bfs(idx, jdx)

    print(ans)