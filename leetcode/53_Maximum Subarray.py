class Solution:

    # 최대 연속 부분합 : 카데인 알고리즘
    def maxSubArray(self, nums: List[int]) -> int:
        maxv = -sys.maxsize
        currsum = 0
        for i in range(len(nums)):
            currsum = max(nums[i], currsum + nums[i])
            maxv = max(maxv, currsum)
        return maxv





