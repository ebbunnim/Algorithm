from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        Q = deque()

        if k == 0:  # 예외처리1
            return []
        if k == 1:  # 2
            return nums

        def clear(i):
            if Q and Q[0] == (i - k):  # 1. pop for staying len
                Q.popleft()
            while Q and nums[Q[-1]] < nums[i]:  # 2. rm smaller value
                Q.pop()
            Q.append(i)  # 3. append

        # start window
        for i in range(k):
            clear(i)
        res = []
        res.append(nums[Q[0]])

        for i in range(k, len(nums)):
            clear(i)
            res.append(nums[Q[0]])

        return res


