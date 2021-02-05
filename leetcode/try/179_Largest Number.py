class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))

        # if set(nums)==set('0'): '00'->'0'
        #     return '0'

        # str형 숫자를 어떤 순으로 이어 붙여야 하는지 확인 #
        def to_swap(a, b):
            return str(a) + str(b) > str(b) + str(a)

        # insertionsort
        for i in range(1, len(nums)):
            for j in range(i, 0, -1):
                if to_swap(nums[j], nums[j - 1]):
                    nums[j], nums[j - 1] = nums[j - 1], nums[j]
        return str(int(''.join(nums)))