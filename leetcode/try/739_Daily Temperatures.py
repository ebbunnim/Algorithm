# 단방향 일때, 투포인터보다 스택을 먼저 생각해보자

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(T)
        for i in range(len(T)):
            while stack and T[stack[-1]] < T[i]:
                idx = stack.pop()
                ans[idx] = i - idx
            stack.append(i)
        return ans
