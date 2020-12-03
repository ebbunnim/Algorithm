class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        strs, nums = [], []
        for log in logs:
            if log.split()[1].isdigit():
                nums+=[log]
            else:
                strs+=[log]
        strs.sort(key=lambda x : (x.split()[1:],x.split()[0]))
        return strs+nums
        