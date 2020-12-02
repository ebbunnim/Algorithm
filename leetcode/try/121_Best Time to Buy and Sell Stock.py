class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 순서대로 진행해야 함.
        profit=0
        minv=sys.maxsize
        for price in prices:
            minv = min(minv,price)
            profit = max(profit, price-minv)
        return profit