class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        i = 0
        total= 0
        maxsub = 0

        for j in range(n):
            if prices[j] < prices[i]:
                i = j
            
            else:
                total = prices[j] - prices[i]
                maxsub = max(maxsub,total)

        return maxsub
            
