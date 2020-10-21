from collections import defaultdict
from copy import deepcopy

flag = 0
ans = []

def solution(tickets):
    global ans, flag
    graph = defaultdict(list)
    vis = defaultdict(list)
    tickets.sort()

    for ticket in tickets:
        graph[ticket[0]].append(ticket[1])
        vis[ticket[0]].append(False)
    res = ['ICN']

    def dfs(start, cnt):
        global flag, ans

        if flag == 1:
            return

        if cnt == len(tickets):
            ans = deepcopy(res)
            flag = 1
            return

        for i in range(len(graph[start])):
            if vis[start][i] == False:
                vis[start][i] = True
                res.append(graph[start][i])
                dfs(graph[start][i], cnt + 1)
                vis[start][i] = False
                res.pop()

    dfs('ICN', 0)

    return ans