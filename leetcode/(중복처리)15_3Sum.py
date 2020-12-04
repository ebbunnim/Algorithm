class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        ans=[]
        for i in range(n-2):
            if i>0 and nums[i]==nums[i-1]: # 중복처리1
                continue
            
            l, r = i+1, n-1
            while 0<=l<n and 0<=r<n and l<r:
                sumv=nums[i]+nums[l]+nums[r]
                if sumv<0:
                    l+=1
                elif sumv>0:
                    r-=1
                else:
                    ans+=[[nums[i],nums[l],nums[r]]]
                    l+=1
                    r-=1
                    # 중복처리2
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1
        return ans

