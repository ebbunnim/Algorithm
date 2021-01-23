import sys
input=sys.stdin.readline


if __name__ == '__main__':
    n,k=map(int,input().split())
    coins=[int(input()) for _ in range(n)]
    DP=[0]*(1+k)
    DP[0]=1 # base case
    for coin in coins:
        for idx in range(coin,k+1):
            DP[idx]+=DP[idx-coin]
    print(DP[k])

    # 탑다운 - 메모이제이션. basecase. 끝까지 가봐야 안다.
    # 바텀업 - 이전 계산을 계속 참조하면서 올라감. 끝에서는 알 수 있다.
