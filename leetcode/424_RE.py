from collections import Counter


class Solution:

    def characterReplacement(self, s: str, k: int) -> int:
        counter = Counter()
        left = right = 0
        for right in range(1, len(s) + 1):
            counter[s[right - 1]] += 1
            max_count = counter.most_common(1)[0][1]
            change_char_num = (right - left) - max_count  # 바꿔야 하는 문자의 수
            if change_char_num > k:
                counter[s[left]] -= 1
                left += 1

        return right - left  # 마지막에 right==len(s) 된 상태이므로

    # Before Refactoring
    # def characterReplacement(self, s: str, k: int) -> int:
    #     counter = Counter()
    #     left = right = 0
    #     ans = 0
    #     while right < len(s):
    #         counter[s[right]] += 1
    #         max_count = counter.most_common(1)[0][1]
    #         change_char_num = right - left + 1 - max_count  # 바꿔야 하는 문자의 수
    #         if change_char_num <= k:
    #             ans = max(ans, right - left + 1)
    #         else:
    #             counter[s[left]] -= 1
    #             left += 1
    #         right += 1
    #
    #     return ans



