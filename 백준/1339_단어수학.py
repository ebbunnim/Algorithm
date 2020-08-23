from collections import defaultdict


if __name__ == '__main__':
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    alpha = defaultdict(int)
    for i in range(N):
        for j in range(len(arr[i])):
            alpha[arr[i][j]] += (pow(10,(len(arr[i])-j)-1))
    alpha_key = sorted(alpha, key=alpha.get , reverse=True)
    ans = 0
    v = 9
    for a in alpha_key:
        ans += v*alpha[a]
        v -= 1
    print(ans)