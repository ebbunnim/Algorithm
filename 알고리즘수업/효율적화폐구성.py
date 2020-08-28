N, K = 3, 4
moneys = [3, 5, 7]
moneys.sort()

# K를 money로 만드는데, 최소한의 갯수를 써서 만들어라
# money를 사용해서 DP를 만들고, 걍신해야 함.
D = [10001]*(K+1)
# 시작점
D[0] = 0
for money in moneys:
    if money <= K:
        D[money] = 1 # 갱신한다.
for money in moneys:
    for idx in range(0,K+1):
        if D[idx] != 10001 and idx+money <= K:
            D[idx+money] = min(D[idx+money],D[idx]+1) # 값이 있더라도 최솟값으로 갱신됨. 숫자가 커질 수록 화폐 사용하는게 줄어들 것이므로

if D[K] == 10001:
    print(-1)
else:
    print(D[K])

