import sys
sys.stdin = open('input.txt','r')

if __name__ == '__main__':
    V,E = map(int, input().split())
    INF = int(1e9)
    arr = [[INF]*(1+V) for _ in range(1+V)]
    for i in range(1,V+1):
        arr[i][i] = 0
    for _ in range(E):
        n1,n2 = map(int,input().split())
        arr[n1][n2] = 1
        arr[n2][n1] = 1
    for k in range(1,V+1):
        for a in range(1,V+1):
            for b in range(1,V+1):
                arr[a][b] = min(arr[a][b],arr[a][k] + arr[k][b])
    ans = [INF]*(1+V)
    for i in range(1,1+V):
        res = 0
        for j in range(1,1+V):
            res += arr[i][j]
        ans[i] = res
    print(ans.index(min(ans)))