from collections import defaultdict
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dials = {
            '2':['a','b','c'],
            '3':['d','e','f'],
            '4':['g','h','i'],
            '5':['j','k','l'],
            '6':['m','n','o'],
            '7':['p','q','r','s'],
            '8':['t','u','v'],
            '9':['w','x','y','z']
        }
        stack = []
        ans = []
        def dfs(starti,path,ans):
            if len(path)==len(digits):
                ans+=[path]
                return 
            
            for i in range(starti,len(digits)):
                for j in dials[digits[i]]:
                    dfs(i+1, path+j,ans)
                    
        dfs(0,'',ans)
        return ans