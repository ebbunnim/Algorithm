# 윈도우 k로 잡으면 되는데, 문제는  max
# 1. 새로운 윈도우 만들때 max가 빠지면, 다시 max를 계산하는게 반복된다. 다 n만큼 소요하면 불필요한 시간낭비
# 2. 새로운 윈도우를 만드는 과정은 pop -> insert 순
# 3. insert하는 것은 문제가 없어. 근데, 나보다 이미 작은 애가 있다면 걔네들은 앞으로도 쓰지 않을 것이므로 모두 삭제
# 4. (x-k)가 window에 들어있다면, 걔는 max값이었는데 윈도우 밖이므로 지워야 하는 원소
# 윈도우는 처음 k를 잡는게 중요하다.-> k가 안될때는 어떻게 할지도 고려해야

from collections import deque


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        window = deque()  # index 기준
        res = []

        def clear_when_insert(x):
            if window and window[0] == (x - k):  # max값이었어도 윈도우 밖이면 out
                window.popleft()
            while window and nums[x] > nums[window[-1]]:
                window.pop()
            window.append(x)

        # make k window
        for i in range(k):
            clear_when_insert(i)
        res.append(nums[window[0]])

        for i in range(k, len(nums)):
            clear_when_insert(i)
            res.append(nums[window[0]])

        return res




