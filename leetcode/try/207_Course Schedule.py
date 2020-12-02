from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        for ele in prerequisites:
            graph[ele[0]] += [ele[1]]

        def dfs(parent):  # g = 자식 노드 리스트
            if parent in traced:
                return False

            if parent in vis:
                return True

            traced.add(parent)
            for child in graph[parent]:
                if child not in traced:
                    dfs(child)
                else:
                    return False
            # 백트래킹
            traced.remove(parent)
            vis.add(parent)  # 순환사이클 없는 노드 저장. 다음 번에 호출되면 바로 True 반환하도록
            return True

        traced = set()
        vis = set()
        # vis를 관리하고 싶었으나, 몇번 노드로 들어올지 모름
        for parent in list(graph):
            if dfs(parent) == False:
                return False
        return True





