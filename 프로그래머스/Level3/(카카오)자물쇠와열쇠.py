def solution(key, lock):
    M = len(key)
    N = len(lock)
    back_len = N + (M - 1) * 2

    def rotate(arr):
        res = [[0] * M for _ in range(M)]
        for r in range(M):
            for c in range(M):
                res[c][M - 1 - r] = arr[r][c]
        return res

    def isfit(start_r, start_c, key, lock):
        back_arr = [[0] * back_len for _ in range(back_len)]  # 항상초기화해야

        # M은 항상 N보다 작다.
        # key의 값으로 back_arr를 부분 초기화한다.
        for i in range(M):
            for j in range(M):
                back_arr[start_r + i][start_c + j] = key[i][j]
        for i in range(M - 1, M - 1 + N):  # lock이 있는 위치
            for j in range(M - 1, M - 1 + N):
                # if back_arr[i][j] or lock[i-(M-1)][j-(M-1)] :
                if back_arr[i][j] + lock[i - (M - 1)][j - (M - 1)] == 1:
                    pass
                else:
                    return False

        return True

    for _ in range(4):  # 최대 4번을 시계방향으로 90도 돌린다.
        key = rotate(key)

        for r in range(back_len - M + 1):  # 인덱스 유의
            for c in range(back_len - M + 1):
                # (r, c)는 시작점
                if isfit(r, c, key, lock):
                    return True
    return False
