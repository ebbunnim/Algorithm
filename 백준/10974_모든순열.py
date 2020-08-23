def dfs(start):
    if False not in vis:
        print(' '.join(list(map(str,ans))))
        return

    for i in range(N):
        if vis[i] == False:
            vis[i] = True
            ans.append(N_list[i])
            dfs(start+1)
            vis[i] = False
            ans.pop()


if __name__ == '__main__':
    N = int(input())
    N_list = [ i for i in range(1,N+1) ]
    vis = [False]*N
    ans = []
    dfs(0)
