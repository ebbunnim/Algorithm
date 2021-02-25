from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mydict = defaultdict(list)
        for s in strs:
            _s = ''.join(sorted(s))
            mydict[_s]+=[s]
        return mydict.values()