class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def dfs(res, start, k):
            if k == 0:
                ans.append(res[:])
                return

            for i in range(start, n + 1):  # start가 중요했음. 나와 *내 앞요소들을(순열과 차이)* 배제하고 next_elements 구성함.
                res.append(i)
                dfs(res, i + 1, k - 1)  # 리스트는 mutable. 문자열은 값 할당해버리면 백트래킹 안되는데 배열은 되는 이유
                res.pop()

        dfs([], 1, k)
        return ans


    # sol2
    # return list(combinations([i for i in range(1, n + 1)], k))