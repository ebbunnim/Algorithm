from itertools import combinations

if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    combs = list(combinations([i for i in range(1, N + 1)], N // 2))
    point = len(combs) // 2

    starts = combs[:point]
    links = sorted(combs[point:], reverse=True)
    min = 9999999999999999999
    for i in range(len(starts)):
        s, l = 0, 0
        for a in range(N // 2):
            for b in range(N // 2):
                s += arr[starts[i][a] - 1][starts[i][b] - 1]
                l += arr[links[i][a] - 1][links[i][b] - 1]
        if abs(s - l) < min:
            min = abs(s - l)
    print(min)
​