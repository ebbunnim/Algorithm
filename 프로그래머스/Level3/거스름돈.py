# max로 뽑아낼거야. 그리고 갱신할때는 새 값이 아니라 + 1
def solution(n, money):
    L = len(money)
    D = [0] * (n + 1)
    # D[i] = D[i] + D[i-mon]
    for mon in money:
        for i in range(1, n + 1):
            if i == mon:
                D[i] += 1
            if 0 <= i - mon:
                D[i] = D[i] + D[i - mon]
    return D[n]