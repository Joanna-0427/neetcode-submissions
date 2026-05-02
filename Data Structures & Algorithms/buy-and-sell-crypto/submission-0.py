class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left, right = 0, 1
        maxP = 0
        while right < len(prices) :
            if prices[left] < prices[right]:
                value = prices[right]- prices[left]
                maxP = max(maxP,value)
                right += 1
            else:
                left = right
                right = left + 1
        return maxP
        