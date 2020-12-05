class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        D = {
            '(':')',
            '[':']',
            '{':'}'
        }
        for e in s:
            if e in D.keys():
                stack.append(e)
            else:
                if not stack or e!=D[stack.pop()]:
                    return False
        return stack==[]
        
        
    # 완전히 순회하고 나서야 T/F 판별할 수 있음. 최적화 필요 
    # def isValid(self, s: str) -> bool:
    #     stack=[]
    #     for _s in s:
    #         if _s==')':
    #             if stack and stack[-1]=='(':
    #                 stack.pop()
    #                 continue
    #         elif _s=='}':
    #             if stack and stack[-1]=='{':
    #                 stack.pop()
    #                 continue
    #         elif _s==']':
    #             if stack and stack[-1]=='[':
    #                 stack.pop()
    #                 continue
    #         stack.append(_s)
    #     if stack==[]:
    #         return True
    #     else:
    #         return False
            
            
        