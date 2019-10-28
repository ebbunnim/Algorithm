import sys
sys.stdin = open("input.txt","r")

def notwall(x, y): #새로갈 인덱스
    return 0<=x<N and 0<=y<N

def matprint(arr):
    for i in range(len(arr)):
        print(arr[i])

def search(x, y):
    dx = [-1, -1, -1, 0, 0, 1, 1, 1]
    dy = [-1, 0, 1, -1, 1, -1, 0, 1]
    flag = 0

    for i in range(8):
        flag = 0
        new_x = x + dx[i]
        new_y = y + dy[i]

        if notwall(new_x, new_y):
            # 같은 색이라면,
            if arr[new_x][new_y] == arr[x][y]:
                continue
            elif arr[new_x][new_y] == 0:
                continue
            else: #다른 색이라면,
                temp_store = [(new_x,new_y)]
                new_x += dx[i]
                new_y += dy[i]
                while notwall(new_x, new_y): #벽에 닿는 순간까지
                    # 같은 색을 찾으면 탐색을 종료한다,
                    if arr[new_x][new_y] == arr[x][y]:
                        flag = 1
                        break
                    elif arr[new_x][new_y] == 0:
                        break
                    else:
                        temp_store.append((new_x, new_y))
                        new_x += dx[i]
                        new_y += dy[i]
                        continue

                if flag == 1:
                    for item in temp_store:
                        arr[item[0]][item[1]] = arr[x][y]

    return arr

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [[0]*N for _ in range(N)]

    arr[N//2-1][N//2-1] = 2; arr[N//2-1][N//2] = 1;
    arr[N//2][N//2-1] = 1; arr[N//2][N//2] = 2;



    for i in range(M):
        col, row, color = map(int, input().split())
        arr[row-1][col-1] = color
        search(row-1, col-1)

    white = 0
    black = 0
    for a in range(N):
        for b in range(N):
            if arr[a][b] == 1:
                black += 1
            elif arr[a][b] == 2:
                white += 1

    print('#%d %d %d' % (tc,black, white))


