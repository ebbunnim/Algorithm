from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        D=defaultdict(list)
        for course in prerequisites:
            D[course[0]]+=[course[1]]
        starters = set()
        vis_node = set()
        
        def dfs(start):
            if start in starters:
                return 
            if start in vis_node:
                return True
            
            starters.add(start)
            for nxt in D[start]:
                if not dfs(nxt): # false뜨면 이전에 호출된 함수 모두가 false 반환
                    return 
                
            # dfs가 모든 nxt 노드들을 정상적으로 거쳤다면. 다시 상위 노드로 가기 전에
            starters.remove(start)
            vis_node.add(start)
            return True
        
        # 어떤 노드가 시작점인지 모름
        for start in list(D):
            if not dfs(start):
                return False
        return True



