def dfs(start_node, row):
    global ans, min

    if ans > min:  # 가지치기
        return

    if start_node == row and False not in vis:
        if ans < min:
            min = ans
        return

    for j in range(N):  # 열 (end_node임)
        if vis[j] == False and arr[start_node][j] != 0:
            vis[j] = True
            ans += arr[start_node][j]
            dfs(j, row)
            vis[j] = False
            ans -= arr[start_node][j]  # 탈출조건에서 ans=0 해버리면 1 2 3 -> 1 3 2 될때 1이 고려 안됨 주의


if __name__ == '__main__':
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    vis = [False] * N
    min = 9999999999999999999
    ans = 0

    for i in range(N):
        dfs(i, i)
    print(min)
