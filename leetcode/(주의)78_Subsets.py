class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        def dfs(start,stack,ans):
            ans+=[stack] # stack.pop() 논리로 가지 않는 이상, 재귀에서의 모든 시간의 stack이 표현한 객체(id가 달라짐)가 들어있는 것
            for i in range(start,len(nums)):
                dfs(i+1,stack+[nums[i]],ans)
            
        dfs(0,[],ans)
        return ans
            