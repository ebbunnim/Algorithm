# O(n)으로 풀어야 함
from copy import deepcopy
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n=len(nums)
        output=deepcopy(nums)
        t=1
        for i in range(n):
            output[i]=t
            t*=nums[i]
        t=1
        for i in range(n-1,-1,-1):
            output[i]*=t
            t*=nums[i]
        return output