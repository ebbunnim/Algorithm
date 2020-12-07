from collections import Counter
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans=[]
        counter = Counter(nums)
        heap=[]
        for key in counter:
            heapq.heappush(heap,(-counter[key],key))
        for _ in range(k):
            if heap:
                ans+=[heapq.heappop(heap)[1]]
        return ans
        
        # sol2
        # return list(zip(*Counter(nums).most_common(k)))[0]        
