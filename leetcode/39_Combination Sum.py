class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # 중복 조합. 합이 정해짐
        # 백트래킹 - 정렬 후 넘어서면
        candidates.sort()
        ans=[]
        def dfs(start,sumv,stack,ans):
            if sumv > target:
                return 
            
            if sumv==target:
                ans+=[tuple(stack)]
            
            
            for i in range(start,len(candidates)):
                stack+=[candidates[i]]                
                dfs(i,sumv+candidates[i],stack,ans)
                stack.pop()
                
        dfs(0,0,[],ans)
        return ans