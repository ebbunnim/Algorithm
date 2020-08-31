def solution(n):
    D = [1] * (n + 1)
    D[1] = 1
    for i in range(2, n + 1):
        D[i] = D[i - 1] + D[i - 2]

    return D[n] % 1234567