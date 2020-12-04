class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 한 시점에서는 바로 샀음을 가정. 모두 공개된 정보라고 가정했으므로 
        maxv = 0
        minv = 1e9
        for i in range(len(prices)):
            # 최소값 교체
            if prices[i]<minv:
                minv=prices[i]
            # 최대 연산값 교체
            if prices[i]>minv:
                maxv=max(maxv,prices[i]-minv)
        return maxv       
        
        
        