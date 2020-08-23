if __name__ == '__main__':
    T = int(input())
    left = 1000-T
    coins = [500, 100, 50, 10, 5, 1]
    ans = 0
    for coin in coins:
        count, result = divmod(left, coin)
        left = result
        ans += count
    print(ans)