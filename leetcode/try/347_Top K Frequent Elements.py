from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Sol1
        counter = Counter(nums)
        heap = []
        res = []
        for c in counter:
            heap.append((-counter[c], c))  # 빈도, 원소
        heapq.heapify(heap)
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res

        # Sol2
        counter = Counter(nums)
        return list(zip(*counter.most_common(k)))[0]
