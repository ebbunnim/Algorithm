if __name__ == '__main__':
    T = int(sys.stdin.readline())
    D = [[0] * 4 for _ in range(100001)]
    D[1][1] = 1
    D[1][2] = 0
    D[1][3] = 0
    D[2][1] = 0
    D[2][2] = 1
    D[2][3] = 0
    D[3][1] = 1
    D[3][2] = 1
    D[3][3] = 1

    for i in range(4, 100001):
        D[i][1] = (D[i - 1][2] + D[i - 1][3]) % 1000000009
        D[i][2] = (D[i - 2][1] + D[i - 2][3]) % 1000000009
        D[i][3] = (D[i - 3][1] + D[i - 3][2]) % 1000000009

    for t in range(T):
        N = int(sys.stdin.readline())
        print(sum(D[N])%1000000009)