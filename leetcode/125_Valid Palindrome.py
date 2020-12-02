# isalnum() 이 관건!

class Solution:
    def isPalindrome(self, s: str) -> bool:
        strs = []
        for ele in s:
            if ele.isalnum():
                strs+=[ele.lower()]
        if strs[::-1]==strs:
            return True
        else:
            return False
        