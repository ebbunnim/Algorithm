class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<2 and s[:]==s[::-1]:
            return s
        
        n = len(s)
        # 팰린 판별과 투포인터 확장
        def expand(l,r):
            while 0<=l and r<=n and s[l]==s[r-1]:
                l-=1
                r+=1   
            return s[l+1:r-1] # expand 안되는 애들이 l,r이니까
        
        res=''
        for l in range(n-1):
            res=max(res,expand(l,l+1),expand(l,l+2),key=len) # 홀수, 짝수 
        return res
