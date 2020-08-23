if __name__ == '__main__':
    N = int(input())
    P = list(map(int, input().split())) # 접근할 때는 -1로 따로 관리
    D = [0]*1001
    for i in range(1, N+1):
        if i == 1:
            D[i] = P[0]
        else:
            D[i] = P[i-1]
            for j in range(i): # 1 ~ 4가 됨. P 인덱스는 0 ~3까지 됨.
                if D[i] > P[i-j-1] + D[j]:
                    D[i] = P[i-j-1] + D[j]
    print(D[N])