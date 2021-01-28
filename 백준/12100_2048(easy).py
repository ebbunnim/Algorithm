from collections import deque

def up(arr):
    narr = [[0] * N for _ in range(N)]
    for j in range(N):
        Q = deque()
        for i in range(N):
            if arr[i][j] != 0:
                Q.append(arr[i][j])
        k = 0
        while Q:
            num = Q.popleft()
            if narr[k][j] == 0:
                narr[k][j] = num
            else:
                if num == narr[k][j]:
                    narr[k][j] += num
                    k += 1
                else:
                    k += 1
                    narr[k][j] = num
    return narr

def down(arr):
    narr = [[0] * N for _ in range(N)]
    for j in range(N):
        Q = deque()
        for i in range(N - 1, -1, -1):
            if arr[i][j] != 0:
                Q.append(arr[i][j])
        k = N - 1
        while Q:
            num = Q.popleft()
            if narr[k][j] == 0:
                narr[k][j] = num
            else:
                if num == narr[k][j]:
                    narr[k][j] += num
                    k -= 1
                else:
                    k -= 1
                    narr[k][j] = num
    return narr


def left(arr):
    narr = [[0] * N for _ in range(N)]
    for i in range(N):
        Q = deque()
        for j in range(N):
            if arr[i][j] != 0:
                Q.append(arr[i][j])
        k = 0
        while Q:
            num = Q.popleft()
            if narr[i][k] == 0:
                narr[i][k] = num
            else:
                if num == narr[i][k]:
                    narr[i][k] += num
                    k += 1
                else:
                    k += 1
                    narr[i][k] = num
    return narr


def right(arr):
    narr = [[0] * N for _ in range(N)]
    for i in range(N):
        Q = deque()
        for j in range(N - 1, -1, -1):
            if arr[i][j] != 0:
                Q.append(arr[i][j])
        k = N - 1
        while Q:
            num = Q.popleft()
            if narr[i][k] == 0:
                narr[i][k] = num
            else:
                if num == narr[i][k]:
                    narr[i][k] += num
                    k -= 1
                else:
                    k -= 1
                    narr[i][k] = num
    return narr

def dfs(arr,cnt):
    global maxv
    if cnt == 5:
        for row in arr:
            maxv = max(maxv,max(row))
        return
    for func in (up,down,left,right):
        dfs(func(arr),cnt+1)

if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    maxv = 0
    dfs(arr,0)
    print(maxv)