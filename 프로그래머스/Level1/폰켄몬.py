from collections import Counter

def solution(nums):
    N = len(nums)//2
    counter = Counter(nums)
    if len(counter.keys()) < N:
        return len(counter.keys())
    else:
        return N