from collections import Counter
class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        counter = Counter(S)
        ans=0
        for j in set(J):
            if j in counter:
                ans+=counter[j]
        return ans