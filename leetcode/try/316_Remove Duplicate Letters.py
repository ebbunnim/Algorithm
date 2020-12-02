from collections import Counter


# 알파벳 순서를 보되, 빈도수도 함께 고려해야 하는 문
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # stack에 넣되, 마지막 애보다 현재가 더 알파벳상 앞서고, 마지막 애를 다시 쓸 수 있었다면(count>0) pop하고 현재를 넣는다.
        counter = Counter(list(s))
        stack = []

        for _s in s:
            counter[_s] -= 1
            if _s in stack:
                continue
            # pop 할 것 있나 확인
            while stack and stack[-1] > _s and counter[stack[-1]] > 0:
                stack.pop()
            stack.append(_s)
        return ''.join(stack)
