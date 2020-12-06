from collections import Counter
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        counter = Counter(s)
        stack = []
        vis=set()
        for ele in s:
            counter[ele]-=1
            if ele in vis:
                continue
            while stack and counter[stack[-1]]>=1 and stack[-1]>ele:
                vis.remove(stack.pop())
            stack.append(ele)
            vis.add(ele)
        return ''.join(stack)           