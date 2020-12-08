class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:        
        stack=[]
        ans=[]
        
        def dfs(start,ans):
            if len(stack)==k:
                ans+=[tuple(stack)]
                return 
            
            for i in range(start,n+1):
                stack.append(i)
                dfs(i+1,ans)
                stack.pop()
                
        dfs(1,ans)
        return ans