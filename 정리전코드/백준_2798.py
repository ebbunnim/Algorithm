import sys
sys.stdin = open("input.txt", "r")

# 3개를 조합으로 뽑음.
# 제약 - M을 넘으면 안됨


N, M = map(int, input().split())
cards = list(map(int, input().split()))
ans = 9999999
# print(cards)


for i in range(N):
    for j in range(i+1, N):
        for z in range(j+1, N):
            tmp = cards[i] + cards[j] + cards[z]
            if tmp <= M:
                if abs(tmp-M) < ans:
                    ans = abs(tmp-M)
                    res = tmp
print(res)
