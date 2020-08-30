def solution(triangle):
    for i in range(1, len(triangle)):
        N = len(triangle[i])
        for j in range(N):
            if j == 0:
                triangle[i][j] += triangle[i - 1][j]
            elif j == N - 1:
                triangle[i][j] += triangle[i - 1][j - 1]
            else:  # 1~n-2
                # print(triangle[i-1][j+1-2])
                triangle[i][j] = max(triangle[i][j] + triangle[i - 1][j - 1], triangle[i][j] + triangle[i - 1][j])

    return max(triangle[-1])