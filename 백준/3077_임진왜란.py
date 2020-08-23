
from collections import defaultdict

if __name__ == '__main__':
    N = int(input())
    first = input().split()
    second = input().split()
    D1 = defaultdict(int)
    D2 = defaultdict(int)

    for idx, val in enumerate(first):
        D1[val] = idx
    for idx, val in enumerate(second):
        D2[val] = idx

    ans = 0
    for i in range(N):
        for j in range(i+1,N):
            if D1[first[i]] < D1[first[j]]:
                if D2[first[i]] < D2[first[j]]: # 순서가 같다.
                    ans += 1

            else:
                if D2[first[i]] > D2[first[j]]:
                    ans += 1
    print(str(ans) + '/' + str(N*(N-1)//2))
