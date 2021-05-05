import sys
input = sys.stdin.readline

n, k = map(int, input().split())
num_list = []
dp = [0 for _ in range(k + 1)]
dp[0] = 1

for i in range(n):
    num_list.append(int(input()))

for num in num_list:
    for i in range(1, k + 1):
        if i >= num:
            dp[i] += dp[i - num]

print(dp[-1])