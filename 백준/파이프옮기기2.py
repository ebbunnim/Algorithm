if __name__ == '__main__':
    # 방향 : 동쪽, 남쪽, 대각선(동쪽방향)
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # arr에서 상태확인 : 움직인 다음에 확인. 특히 대각선은 좌,
    # 스타트는 끝점
    # 경우의 수는, 깊이가 아니라 0,1,2 순으로 몇개가 들어오는지 확인하는 것임
    D = [[[0]*3 for _ in range(N)] for _ in range(N)]
    # 0 (가로) D[r][c][0] = D[r][c-1][1] + D[r][c-1][2]
    # 1 (세로) D[r][c][1] = D[r-1][c][0] + D[r-1][c][2]
    # 2 (대각선) D[r][c][2] = D[r-1][c-1][0] + D[r-1][c-1][1] + D[r-1][c-1][2]

    D[0][1][0] = 1
    for i in range(2,N):
        if arr[0][i] == 0:
            D[0][i][0] = D[0][i-1][0]
    for r in range(1,N):
        for c in range(2,N):
            if arr[r][c] == 0:
                D[r][c][0] = D[r][c - 1][0] + D[r][c - 1][2]
                D[r][c][1] = D[r - 1][c][1] + D[r - 1][c][2]
            if arr[r][c] == 0 and arr[r-1][c] == 0 and arr[r][c-1] == 0:
                D[r][c][2] = D[r - 1][c - 1][0] + D[r - 1][c - 1][1] + D[r - 1][c - 1][2]



    print(D[N-1][N-1][0]+D[N-1][N-1][1]+D[N-1][N-1][2])
