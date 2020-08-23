if __name__ == '__main__':
    N = int(input())
    T = [0]*N
    P = [0]*N
    DP = [0]*(N+5)
    for i in range(N):
        a,b = map(int,input().split())
        T[i], P[i] = a, b
    for i in range(N-1,-1,-1):
        if i+T[i] > N:
            DP[i] = DP[i+1]
        else:
            DP[i] = max(DP[i+1], P[i]+DP[i+T[i]])
    print(DP[0])
