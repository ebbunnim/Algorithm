if __name__ == '__main__':
    k, v = list(map(int, input().split()))
    coins = [0]*k
    for i in range(k):
        coins[i] = int(input())
    ans = 0
    for i in range(k-1, -1, -1):
        count, result = divmod(v,coins[i])
        v = result
        ans += count
    print(ans)