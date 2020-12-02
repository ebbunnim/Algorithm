from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 중복이 나오면 left 움직여. 아니면 right만 우측 이동
        # 실패하면, 중복원소 다음부터 다시 시작해야 돼 - 해시로 저장해놓기
        L = len(s)
        if L == 0:
            return 0
        elif L == 1:
            return 1
        vis = defaultdict(int)
        start = 0  # left 역할
        maxlen = 0
        for idx, val in enumerate(s):  # right 역할
            if val in vis and start <= vis[val]:  # start<=vis[val]이 없으면 'abba'처리 못함. 슬라이딩 안에 있어야
                maxlen = max(maxlen, idx - start)
                start = vis[val] + 1  # 어디로 초기화? 중복된 애 바로 뒤 인덱스로
                vis[val] = idx
            else:
                vis[val] = idx
        maxlen = max(maxlen, len(s) - start)
        return maxlen


