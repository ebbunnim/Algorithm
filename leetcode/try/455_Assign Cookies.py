class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()  # cookie

        s_idx = g_idx = 0
        res = 0
        while True:
            if s_idx == len(s) or g_idx == len(g):
                break
            if s[s_idx] >= g[g_idx]:
                g_idx += 1
                s_idx += 1
                res += 1
            else:
                s_idx += 1  # 만족 못시킨 chind 인덱스는 제자리
        return res
