def dfs(start,i):
    global cnt, res, ans

    if cnt == i:
        if res == S:
            ans += 1
        return

    for j in range(start,N):
        if vis[j] == False:
            vis[j] = True
            res += N_list[j]
            cnt += 1
            dfs(j,i) # combinations 이므로 j로 탐색 출발을 제한함
            vis[j] = False
            res -= N_list[j]
            cnt -= 1

if __name__ == '__main__':
    N,S = map(int,input().split())
    N_list = list(map(int,input().split()))
    vis = [False]*N
    cnt = 0
    res = 0
    ans =0
    for i in range(1,N+1): # 이건 뽑는 개수
        dfs(0,i)
    print(ans)