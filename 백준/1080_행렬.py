
def change(arr, i, j):
    for a in range(3):
        for b in range(3):
            if arr[i+a][j+b] == False:
                arr[i+a][j+b] = True
            else:
                arr[i+a][j+b] = False


if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = [[False]*M for _ in range(N)]
    before = [ list(map(int, input())) for _ in range(N)]
    after = [ list(map(int, input())) for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if before[i][j] != after[i][j]:
                arr[i][j] = True


    cnt=0
    # 2칸 더 뒤에는 끝자리인데, 여기가 False이면 안됨.
    for i in range(N-2):
        for j in range(M-2):
            if arr[i][j] == True:
                change(arr, i, j)
                cnt+=1
            if j == M-2: # 여기까지 걸렸을 때는 이렇게 해야 함.
                if arr[i][j] == True:
                    print(-1)
    if arr == [[False]*M for _ in range(N)]:
        print(cnt)
    else:
        print(-1)
