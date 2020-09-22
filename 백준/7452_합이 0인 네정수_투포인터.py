import sys
sys.stdin = open('input.txt','r')

from collections import defaultdict

if __name__ == '__main__':
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    D1 = defaultdict(int)
    D2 = defaultdict(int)
    for i in range(n):
        for j in range(n):
            D1[arr[i][0]+arr[j][1]] += 1
            D2[arr[i][2]+arr[j][3]] += 1
    D1_keys = sorted(D1)
    D2_keys = sorted(D2)
    s, e = 0, len(D2_keys)-1

    ans = 0
    while True:
        res = D1_keys[s]+D2_keys[e]
        if res < 0:
            s += 1
        else:
            if res == 0:
                ans += D1[D1_keys[s]]*D2[D2_keys[e]]
            e -= 1
        if s == len(D1_keys) or e == -1:
            break
    print(ans)