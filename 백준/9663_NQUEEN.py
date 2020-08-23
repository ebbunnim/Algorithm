def queen(i):
    global ans

    if i == N:
        ans += 1
        return

    for j in range(N): # 열만 순회
        if not (vertical[j] or rightcross[i-j+N-1] or leftcross[i+j]):
            vertical[j], rightcross[i-j+N-1], leftcross[i+j] = True, True, True
            arr[i][j] = 1
            queen(i+1)
            vertical[j], rightcross[i-j+N-1], leftcross[i+j] = False, False, False
            arr[i][j] = 0



if __name__ == '__main__':
    N = int(input())
    arr = [[0]*N for _ in range(N)]
    vertical = [False]*N
    rightcross = [False]*(2*N-1)
    leftcross = [False]*(2*N-1)
    ans = 0

    queen(0) # 첫번째 행부터 시작함.

    print(ans)
