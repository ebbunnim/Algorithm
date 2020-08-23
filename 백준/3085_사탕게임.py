
def check(ans):
    # 열 기준 연속적인 수 갯수 확인
    for a in range(N):
        cnt = 1
        for b in range(1,N):
            if arr[a][b] == arr[a][b-1]:
                cnt += 1
            else:
                if ans < cnt:
                    ans = cnt
                cnt = 1
        if ans < cnt:
            ans = cnt

    # 행 기준 연속적인 수 갯수 확인
    for a in range(N):
        cnt = 1
        for b in range(1,N):
            if arr[b][a] == arr[b-1][a]:
                cnt += 1
            else:
                if ans < cnt:
                    ans = cnt
                cnt = 1
        if ans < cnt:
            ans = cnt

    return ans



if __name__ == '__main__':
    global ans
    ans = 0
    N = int(input())
    arr = [ list(input()) for _ in range(N) ]

    # 행 기준 변경
    for i in range(N):
        for j in range(1,N):
            arr[j][i], arr[j - 1][i] = arr[j - 1][i], arr[j][i]
            ans = check(ans)
            arr[j][i], arr[j - 1][i] = arr[j - 1][i], arr[j][i]

    # 열 기준 변경
    for i in range(N):
        for j in range(1,N):
            arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]
            ans = check(ans)
            arr[i][j], arr[i][j - 1] = arr[i][j - 1], arr[i][j]

    print(ans)