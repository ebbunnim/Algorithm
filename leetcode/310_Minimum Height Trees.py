from collections import deque, defaultdict


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 1:
            return [0]

        graph = defaultdict(list)
        for edge in edges:
            graph[edge[0]] += [edge[1]]
            graph[edge[1]] += [edge[0]]

        leaf_node = deque()
        for key in graph:
            if len(graph[key]) == 1:
                leaf_node.append(key)

        while n > 2:
            m = len(leaf_node)
            for _ in range(m):
                leaf = leaf_node.popleft()
                nxt = graph[leaf].pop()
                graph[nxt].remove(leaf)
                if len(graph[nxt]) == 1:
                    leaf_node.append(nxt)
            n -= m

        return [x for x in leaf_node]



