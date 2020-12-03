from collections import defaultdict
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = defaultdict(int)
        for idx, val in enumerate(nums):
            dic[val]=idx
        for idx, val in enumerate(nums):
            if ((target-val) in dic) and dic[target-val]!=idx:
                return [idx,dic[target-val]]
                
            