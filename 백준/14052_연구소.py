from collections import deque
from copy import deepcopy

#bfs
def virus(copyarr, copyviruslist):
    cnt_virus = 0
    while copyviruslist: # 큐 역할
        x, y = copyviruslist.popleft()
        cnt_virus+=1

        # 가지치기
        if cnt_virus > minv:
            return 999999999999

        for dx, dy in [(-1,0),(1,0),(0,-1),(0,1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx<N and 0<=ny<M and copyarr[nx][ny] == 0:
                copyarr[nx][ny] = 2 #vis처리 따로 안해도 되는 이유
                copyviruslist.append((nx,ny))

    return cnt_virus

#dfs
def setwall(cnt):
    global minv
    if cnt == 3:
        # print(*arr, sep='\n')
        copyarr = deepcopy(arr)
        copyviruslist = deepcopy(viruslist)
        # virus
        minv = min(minv,virus(copyarr, copyviruslist))
        return

    for i in range(N):
        for j in range(M):
            if vis[i][j]==False and arr[i][j] ==  0:
                arr[i][j] = 1
                vis[i][j] = True
                setwall(cnt+1)
                arr[i][j] = 0
                vis[i][j] = False



if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [list(map(int,input().split())) for _ in range(N)]
    vis = [[False]*M for _ in range(N)]
    viruslist = deque()
    cnt_wall = 0
    minv = 999999999999
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 2:
                viruslist.append((i,j))
            elif arr[i][j] == 1:
                cnt_wall += 1

    setwall(0)
    print(N*M-(cnt_wall+3+minv))