def dfs(end, cnt_case):
    global cnt,ans

    if cnt == cnt_case:
        D[ans] = True
        return

    for i in range(end,N):
        if vis[i] == False:
            vis[i] = True
            cnt += 1
            ans += S[i]
            dfs(i,cnt_case)
            cnt -=1
            vis[i] = False
            ans -= S[i]


if __name__ == '__main__':
    N = int(input())
    S = list(map(int, input().split()))
    D = [False]*2000001
    cnt = 0
    vis = [False]*N
    ans = 0
    if 1 not in S:
        print(1)
    else:
        for i in range(1,N+1):
            # i개는 뽑는 개수
            dfs(0,i)
        for i in range(1,2000001):
            if D[i] == False:
                print(i)
                break
