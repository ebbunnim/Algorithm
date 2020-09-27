class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 자신보다 왼쪽 요소들 곱해놓기
        # 자신보다 오른쪽 요소들 곱해놓기
        # time limit exceeded : 이전 값들을 곱하는데, 중복되게 덮으면서 곱하면
        # 곱이 누적되도록 p사용
        L = len(nums)
        ans = [1] * L
        p = 1
        for i in range(L):
            ans[i] *= p
            p *= nums[i]

        p = 1
        for i in range(L - 1, -1, -1):
            ans[i] *= p
            p *= nums[i]
        return ans
