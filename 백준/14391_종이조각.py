
if __name__ == '__main__':
    N,M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    max = 0

    # 비트 마스크 활용. 모든 경우의 수에 대해서
    for a in range(1<<(N*M)):
        res = 0
        # 가로
        for i in range(N):
            ans = '0'
            for j in range(M): # 열 우선탐색
                idx = i*M + j # 일직선
                if a & (1<<idx): # 1일때 이어진것들 가로로 취급
                    ans += str(arr[i][idx%M])
                else:
                    res += int(ans)
                    ans = '0'
            res += int(ans) # else 문을 안거친 경우에는 다음 행 가기전에 값을 더한다.
        # 세로
        for j in range(M):
            ans = '0'
            for i in range(N): # 행 우선탐색
                idx = i*M + j
                if a & (1<<idx): # 0일때 이어진것들 세로로 취급
                    res += int(ans)
                    ans = '0'
                else:
                    ans += str(arr[i][idx%M])

            res += int(ans)

        if res > max:
            max = res
    print(max)
