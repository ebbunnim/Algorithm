class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def dfs(start, res):
            ans.append(res[:])

            for i in range(start, len(nums)):
                res.append(nums[i])
                dfs(i + 1, res)
                res.pop()

        dfs(0, [])
        return ans
