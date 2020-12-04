class Solution:
    def maxProfit(self, prices: List[int]) -> int:
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
        
        # 현재 시점에서의 최소값을 갱신
        # 최소값보다 크다면, 바로 바로 차익을 실현해서 최대값 교체 