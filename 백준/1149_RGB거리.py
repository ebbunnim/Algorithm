def dfs(curr_h, curr_c): # 현재 정점, 현재 색깔
    if curr_h == N:
        return 0
    if DP[curr_h][curr_c] != -1:
        return DP[curr_h][curr_c]

    res = INF
    for nxt in range(3):
        if curr_c == nxt:
            continue
        res = min(res, dfs(curr_h + 1, nxt) + costs[curr_h][curr_c])
    DP[curr_h][curr_c] = res
    return res

if __name__ == '__main__':
    N=int(input())
    costs=[list(map(int,input().split())) for _ in range(N)]
    DP=[[-1]*3 for _ in range(N)]
    INF=1e9

    ans=INF
    for color in range(3):
        ans=min(ans,dfs(0,color))
    print(ans)