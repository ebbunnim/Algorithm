from collections import defaultdict

# 취약한 문제. 다시 풀어보기
# 사전순대로 bfs 탐색하는 것 이외로, "경로가 끊기지 않게 순회"하는 거에 초점을 두어야 한다.
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:

        tickets.sort(reverse=True)
        graph = defaultdict(list)
        for ticket in tickets:
            graph[ticket[0]] += [ticket[1]]

        # sol1
        path = []

        def dfs(start):
            while graph[start]:
                dfs(graph[start].pop())  # 자식의 자식의 노드로 타고 들어갈 수 있도록
            path.append(start)  # 더 이상 자식이 없다. 리프노드부터 path에 담는다.(핵심)

        dfs('JFK')
        return path[::-1]

        # sol2
        # 경로가 먼저 끊기는 애들부터 route에 넣어줌
        # route = []
        # stack = ['JFK']
        # while stack:
        #     while graph[stack[-1]]:
        #         x = graph[stack[-1]].pop()
        #         stack.append(x)
        #     route.append(stack.pop())  # 연결이 끊긴 애들부터(리프노드) 순차적으로 들어갈 것
        # return route[::-1]

