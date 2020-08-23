def dfs(start):
    global cnt, max, min

    if cnt == N+1:
        flag = 0
        for i in range(N):
            if bohos[i] == '<':
                if ans[i] < ans[i+1]:
                    pass
                else:
                    flag = 1
                    break
            else:
                if ans[i] > ans[i+1]:
                    pass
                else:
                    flag = 1
                    break
        if flag == 0:
            tmp = ''.join(map(str,ans))
            if int(tmp)> int(max):
                max = tmp
            if int(tmp)< int(min):
                min = tmp

        return

    for i in range(10):
        if vis[i] == False:
            vis[i] = True
            cnt+=1
            ans.append(nums[i])
            dfs(start+1)
            vis[i] = False
            cnt -= 1
            ans.pop()


if __name__ == '__main__':
    N = int(input())
    bohos = input().split()
    nums = [i for i in range(10)]
    vis = [False]*10
    cnt = 0
    ans = []
    max,min = 0, 999999999999999999999999999

    dfs(0)
    print(max)
    print(min)