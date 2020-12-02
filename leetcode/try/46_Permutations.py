from copy import deepcopy


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        # 트리로 접근하면, 리프노드가 순열의 최종 결과다
        # 백트래킹이야? 맞는데 전화번호 문제랑 다른 점? - 같은 노드정보를 부모/자식으로 사용 중이다.
        # vis를 사용하는 이유 : 노드 자체를 부모/자식 노드로 모두 활용할 수 있기 때문이지.
        prev_elements = []
        res = []

        def dfs(elements):
            if len(elements) == 0:
                res.append(prev_elements[:])  # 얕은 복사로 객체 참조가 아닌 값 복사하도록
                return

            for e in elements:  # 루트 노드 지정
                next_elements = deepcopy(elements)
                next_elements.remove(e)
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop()  # 같은 노드들을 부모, 자식 노드로 같이 사용하고 있으므로 되돌려줘야. vis 안쓰고 스택으로 관리

        dfs(nums)
        return res


# Sol2
# from itertools import permutations
#
# class Solution:
#     def permute(self, nums: List[int]) -> List[List[int]]:
#         return list(permutations(nums))