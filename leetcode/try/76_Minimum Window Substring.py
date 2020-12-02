from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = Counter(t)
        missing = len(t)
        left = start = end = 0

        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1  # 얘는 무조건 수행

            if missing == 0:
                while left < right and need[s[left]] < 0:  # T 내부의 알파벳이 나올때까지 left 포인터를 올린다.
                    need[s[left]] += 1
                    left += 1
                # T가 들어있는 범위로 최대한 줄인다.
                if not end or right - left <= end - start:
                    start, end = left, right
                need[s[left]] += 1  # 다른 범위에 T가 들어있어 더 작은 범위의 케이스로 바꿀 수 있는지 순회하기 위해 제자리로
                missing += 1
                left += 1

        return s[start:end]