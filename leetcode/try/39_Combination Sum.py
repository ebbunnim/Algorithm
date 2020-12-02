class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 모든 조합 - 크기가 정해져 있지 않음. target을 만족하는 조합을 구하기
        ans = []

        def dfs(res, sumv):

            # prunning
            if sumv > target:
                return

            if sumv == target:
                if sorted(res) not in ans:  # 중복원소 들어갈 수 있는데, ans에 res가 중복되면 안됨
                    ans.append(sorted(res))
                return

            for i in range(len(candidates)): # start로 제어 안하는 이유 : "중복원소 사용가능"
                res.append(candidates[i])
                dfs(res, sumv + candidates[i])
                res.pop()

        dfs([], 0)  # 이번엔 인덱스로 찾을 예정
        return ans
