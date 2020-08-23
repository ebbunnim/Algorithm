
if __name__ == '__main__':
    N, M = map(int, input().split())
    arr = list(input() for _ in range(5*N+1))

    D = [0,0,0,0,0]
    for i in range(1,5*N+1,5):
        for j in range(1,5*M+1,5):
            start_i = i
            cnt = 0
            while arr[start_i][j]!='#':
                if arr[start_i][j] == '*':
                    cnt += 1
                    start_i += 1
                else:
                    break
            D[cnt] += 1
    print(' '.join(map(str,D)))