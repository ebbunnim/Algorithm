from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        D = defaultdict(list)
        for st in strs:
            tmp = sorted(list(st))
            D[''.join(tmp)].append(st)
        return D.values()