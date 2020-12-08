from itertools import permutations

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        stack=[]
        vis=[False]*len(nums)
        ans=[]
        def dfs(stack,ans):
            if len(stack)==len(nums):
                ans+=[tuple(stack)]
                return 
            
            for i in range(len(nums)):
                if vis[i]==False:
                    stack.append(nums[i])
                    vis[i]=True
                    dfs(stack,ans)
                    stack.pop()
                    vis[i]=False
        dfs(stack,ans)
        return ans