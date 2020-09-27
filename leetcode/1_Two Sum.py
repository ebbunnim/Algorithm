class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # BF하지 말아야 한다.
        D = {}
        for i, num in enumerate(nums):
            if target-num in D:
                return [D[target-num],i]
            D[num] = i
            # D[val] = index
