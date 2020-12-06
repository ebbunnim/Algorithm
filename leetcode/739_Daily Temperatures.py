class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stack = []
        n = len(T)
        output = [0]*n
        for i in range(n):
            while stack and T[stack[-1]]<T[i]:
                before_idx = stack.pop()
                output[before_idx] = i-before_idx
            stack.append(i)
        return output
