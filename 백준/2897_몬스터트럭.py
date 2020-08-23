def locate(x,y):
    cnt = 0
    for dx, dy in (0,0),(1,0),(0,1),(1,1):
        if arr[x+dx][y+dy] == '#':
            return -1
        elif arr[x+dx][y+dy] == 'X':
            cnt += 1
        else:
            pass
    return cnt


if __name__ == '__main__':
    N, M = map(int, input().split())
    D = [0]*5
    arr = [input() for _ in range(N)]
    for i in range(N-1):
        for j in range(M-1):
            if arr[i][j] != '#':
                cnt = locate(i,j)
                if cnt != -1:
                    D[cnt] += 1

    for d in D:
        print(d)
