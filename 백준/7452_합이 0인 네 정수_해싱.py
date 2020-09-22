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
    ans = 0
    for key in D1:
        if D2[-key]:
            ans += (D1[key] * D2[-key])
    print(ans)