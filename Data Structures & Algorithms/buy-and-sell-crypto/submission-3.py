class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l = 0
        maxvalue = 0
        n = len(prices)
        

        for r in range(n):
            if prices[r] > prices[l]:
                maxvalue = max(maxvalue, prices[r] - prices[l])
            else:
                l = r
        return maxvalue
            
            

