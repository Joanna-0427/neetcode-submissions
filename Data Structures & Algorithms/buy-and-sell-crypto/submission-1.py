class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        maxprice = 0
        n = len(prices)
        for right in range(n):
            if prices[left] < prices[right]:
                maxprice = max(prices[right] - prices[left],maxprice)
            else:
                left = right
        return maxprice

