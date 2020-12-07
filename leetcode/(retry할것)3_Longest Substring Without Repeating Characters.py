from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        D=defaultdict(int)
        maxv=start=0
        for idx, val in enumerate(s):
            if val in D and start<=D[val]:
                start = D[val]+1
            else:
                maxv = max(maxv,idx-start+1)
            D[val]=idx
        return maxv

        # <solution2>
        # 중복이 있으면, l이 움직여서 중복 없도록 해야 함.
        # if len(s)==len(set(s)):
        #     return len(s)
        # maxv=1
        # sets = set()
        # l=0
        # sets.add(s[l])
        # for r in range(1,len(s)):
        #     if s[r] not in sets:
        #         sets.add(s[r])
        #         maxv = max(maxv,len(sets))
        #     else: # l 포인터 움직임
        #         while s[r] in sets:
        #             sets.remove(s[l])
        #             l += 1
        #         sets.add(s[r])
        # return maxv
                
            