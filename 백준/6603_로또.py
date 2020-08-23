def dfs(end,K):
    global cnt
    if cnt == 6:
        print(' '.join(map(str,ans)))
        return

    for i in range(K):
        if vis[i] == False and i > end:
            vis[i] = True
            cnt += 1
            ans.append(S[i])
            dfs(i,K)
            vis[i] = False
            cnt -= 1
            ans.pop()
    return


if __name__ == '__main__':
    while True:
        N_list = list(map(int,input().split()))
        if N_list == [0]:
            break
        cnt = 0
        K = N_list[0]
        S = N_list[1:]
        ans = []
        vis = [False]*K
        dfs(-1,K)
        print()
