class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # bit연산은, 버튼을 누르고 다시 되돌리는 것 같다.
        res = 0
        for num in nums:
            res^=num
        return res