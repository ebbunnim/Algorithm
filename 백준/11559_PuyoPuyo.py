
from collections import deque

def bfs(x, y, alpha):
    global flag
    Q = deque()
    Q.append((x,y))
    vis = [[False]*6 for _ in range(12)]
    vis[x][y] = True
    p = 0
    before_p = -1
    while before_p != p :
        x, y = Q[p]
        before_p = p
        for dx, dy in (1,0),(-1,0),(0,1),(0,-1):
            nx = x + dx
            ny = y + dy
            if 0<=nx<12 and 0<=ny<6 and vis[nx][ny] == False and arr[nx][ny] == alpha:
                Q.append((nx,ny))
                vis[nx][ny] = True
                p += 1
    # 터뜨림
    if len(Q)>=4:
        flag = True
        for q in range(len(Q)):
            arr[Q[q][0]][Q[q][1]] = '.'

    return


def go_down():# 3중 포문
    for j in range(6):
        for i in range(11,0,-1):
            if arr[i][j] == '.':
                for k in range(i-1,-1,-1):
                    if arr[k][j] != '.':
                        arr[i][j] = arr[k][j]
                        arr[k][j] = '.'
                        break
    return



if __name__ == '__main__':
    arr = [list(input()) for _ in range(12)]
    flag = True
    ans = 0

    while flag == True: # bfs중 하나라도 터진게 있었다면 flag 를 true로 바꿔놓은 상태
        flag = False
        for i in range(12):
            for j in range(6):
                if arr[i][j] != '.':
                    bfs(i,j,arr[i][j])

    # 뿌요가 터진 케이스가 있다면, 아래로 떨어뜨리고 연쇄횟수에 1을 더한다.
        if flag == True:
            go_down()
            ans += 1
    print(ans)