class Solution:
    def longestPalindrome(self, s: str) -> str:
        # 홀수, 짝수일 경우에 달라진다. 케이스가
        # 두, 세개의 슬라이딩 윈도우를 찾고
        def expand(start, end):  # end가 슬라이싱 인덱스임에 주의
            while 0 <= start and end <= len(s) and s[start] == s[end - 1]:
                start -= 1
                end += 1
            return s[start + 1:end - 1]

        if len(s) == 1:
            return s
        if len(s) == 2 and s[:] == s[::-1]:
            return s

        maxv = ''
        for i in range(len(s) - 1):
            maxv = max(maxv, expand(i, i + 1), expand(i, i + 2), key=len)
        return maxv
