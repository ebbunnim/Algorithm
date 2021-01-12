def check(cnt, status):
    # base case
    if cnt >= P:
        return 0
    if DP[status][cnt] != -1:
        return DP[status][cnt]

    ans = 1e9
    for i in range(N):
        if status & (1 << i):
            for j in range(N):
                if not status & (1 << j):
                    ans = min(ans, check(cnt + 1, status | (1 << j)) + costs[i][j])
    DP[status][cnt] = ans
    return ans


if __name__ == '__main__':
    N = int(input())
    costs = [list(map(int, input().split())) for _ in range(N)]
    onoff = input()
    status = 0
    cnt = 0
    for i in range(N):
        if (onoff[i] == 'Y'):
            status += (1 << i)
            cnt += 1
    P = int(input())
    DP = [[-1] * N for _ in range(1 << N)]

    ans = check(cnt, status)
    print(ans if ans != 1e9 else -1)