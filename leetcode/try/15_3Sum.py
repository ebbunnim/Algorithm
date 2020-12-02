class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        L = len(nums)
        for i in range(len(nums)-2): #i는 멈춘 상태.
            # i가 바로 전 값과 같아 중복된 케이스를 res append하는 것 방지
            if i>0 and nums[i]==nums[i-1]:
                continue
            left, right = i+1, L-1
            while left < right:
                if (nums[i]+nums[left]+nums[right])==0:
                    res.append([nums[i],nums[left],nums[right]])
                    # 중복된 left,right를 res로 포함하지 않도록 처리
                    while left<right and nums[left]==nums[left+1]:
                        left += 1
                    while left<right and nums[right]==nums[right-1]:
                        right -= 1
                    left+=1
                    right-=1
                elif (nums[i]+nums[left]+nums[right]) < 0:
                    left += 1
                else:
                    right -= 1
        return res



