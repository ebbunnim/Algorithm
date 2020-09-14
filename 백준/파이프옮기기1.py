import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    # 방향 : 동쪽, 남쪽, 대각선(동쪽방향)
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    D = [[[0]*3 for _ in range(N)] for _ in range(N)]
    # 가로 0 세로1 대각선 2
    #(1) D[r][c][0] = D[r][c-1][0] + D[r][c-1][2] # 현재 행, 현재 열, 이전 방
    #(2) D[r][c][1] = D[r-1][c][1] + D[r-1][c][2]
    #(3) D[r][c][2] = D[r-1][c-1][0] + D[r-1][c-1][1]+ D[r-1][c-1][2]
    # 전처리
    D[0][1][0] = 1
    for i in range(2,N):
        if arr[0][i] == 0:
            D[0][i][0] = D[0][i-1][0]

    # 벽이 있다는 제약에 주
    for r in range(1,N):
        for c in range(1,N):
            if arr[r][c] == 0: # 현재에 대한 확인
                D[r][c][0] = D[r][c-1][0] + D[r][c-1][2]
                D[r][c][1] = D[r-1][c][1] + D[r-1][c][2]
            if arr[r][c] == 0 and arr[r-1][c] == 0 and arr[r][c-1]==0: # 현재와 바로 전이 현재에 미친 영향을 고려
                D[r][c][2] = D[r - 1][c - 1][0] + D[r - 1][c - 1][1] + D[r - 1][c - 1][2]

    print(D[N-1][N-1][0]+D[N-1][N-1][1]+D[N-1][N-1][2])
