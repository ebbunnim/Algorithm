class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for _s in s:
            if _s==')':
                if stack and stack[-1]=='(':
                    stack.pop()
                    continue
            elif _s=='}':
                if stack and stack[-1]=='{':
                    stack.pop()
                    continue
            elif _s==']':
                if stack and stack[-1]=='[':
                    stack.pop()
                    continue
            stack.append(_s)
        if stack==[]:
            return True
        else:
            return False
            
            
        