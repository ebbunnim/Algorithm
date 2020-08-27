from collections import defaultdict

ans = 'ZZZ'

def solution(tickets):
    N = len(tickets)
    D = defaultdict(list)
    vis = defaultdict(list)

    for i in range(N):
        D[tickets[i][0]] += [tickets[i][1]]
        vis[tickets[i][0]] += [False]

    stack = ['ICN']

    def dfs(key):
        global ans
        if len(stack) == N + 1:
            tmp = ' '.join(stack)
            if tmp < ans:
                ans = tmp
                print(tmp)
            return

        for i in range(len(D[key])):
            curr = D[key][i]
            if vis[key][i] == False:
                vis[key][i] = True
                stack.append(curr)
                dfs(curr)
                stack.pop()
                vis[key][i] = False

    dfs('ICN')

    return ans.split(' ')